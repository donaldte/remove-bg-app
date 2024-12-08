import io
import base64
import logging 
from django.urls import reverse
from rembg import remove
from django.shortcuts import redirect, render
from django.views.generic import TemplateView
from django.http import JsonResponse
from .models import ImageProcessing
from PIL import Image, ImageColor, UnidentifiedImageError


from django.core.files.base import ContentFile


logger = logging.getLogger(__name__)

class MainView(TemplateView):
    """
    Name: MainView
    Description: This view is used to render the main page of the application.
    Author: donaldtedom0@gmail.com
    """
    template_name = 'index.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context
    
    
    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, self.get_context_data())
    
    
    def post(self, request, *args, **kwargs):
        logger.info("Processing image...")
        logger.info(f"Request data: {request.POST}")
        logger.info(f"Request files: {request.FILES}")

        try:
            uploaded_image = request.FILES['image']
            background_color = request.POST.get('background_color', '#FFFFFF')

            # Vérifier le type MIME du fichier
            if uploaded_image.content_type not in ['image/jpeg', 'image/png']:
                return JsonResponse({'error': 'Seuls les fichiers JPEG et PNG sont supportés.'}, status=400)

            # Charger et vérifier l'image
            try:
                input_image = Image.open(uploaded_image)
                input_image.load()
            except Exception as e:
                logger.error(f"Image loading error: {str(e)}")
                return JsonResponse({'error': 'Impossible de charger le fichier comme une image valide.'}, status=400)

            # Vérifier le format
            if input_image.format not in ['JPEG', 'PNG']:
                return JsonResponse({'error': 'Seuls les fichiers JPEG et PNG sont supportés.'}, status=400)

            # Convertir l'image pour rembg
            with io.BytesIO() as buffer:
                input_image.save(buffer, format='PNG')
                image_bytes = buffer.getvalue()

            # Traitement avec rembg
            output = remove(image_bytes)
            output_image = Image.open(io.BytesIO(output))

            # Ajouter une couleur d'arrière-plan
            bg_color = ImageColor.getrgb(background_color)
            bg_image = Image.new("RGBA", output_image.size, bg_color)
            combined = Image.alpha_composite(bg_image, output_image)

            # Sauvegarder l'image traitée
            output_buffer = io.BytesIO()
            combined.save(output_buffer, format='PNG')
            output_buffer.seek(0)
            processed_image_file = ContentFile(output_buffer.read(), name=f"processed_{uploaded_image.name}")

            # Enregistrer dans la base de données
            image_instance = ImageProcessing(
                original_image=uploaded_image,
                processed_image=processed_image_file,
                background_color=background_color,
                ip_address=request.META.get('REMOTE_ADDR')
            )
            image_instance.save()

            # Retourner l'image traitée
            output_buffer.seek(0)
            image_base64 = base64.b64encode(output_buffer.read()).decode('utf-8')
            image_url = f"data:image/png;base64,{image_base64}"

            return JsonResponse({'processed_image': image_url}, status=200)

        except Exception as e:
            logger.error(f"An error occurred: {str(e)}")
            return JsonResponse({'error': 'Une erreur est survenue pendant le traitement de l\'image.'}, status=500)

            
            