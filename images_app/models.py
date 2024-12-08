import os
import uuid
from django.db import models
from django.core.exceptions import ValidationError



class ImageProcessing(models.Model):
    name = models.CharField(max_length=100, unique=True, blank=True)  # Rempli automatiquement
    original_image = models.ImageField(upload_to='uploads/')
    processed_image = models.ImageField(upload_to='processed/', blank=True, null=True)
    background_color = models.CharField(max_length=7, default='#FFFFFF')  # default is white
    uploaded_at = models.DateTimeField(auto_now_add=True)
    ip_address = models.GenericIPAddressField(blank=True, null=True)

    def __str__(self):
        return f"Image {self.name}"

    class Meta:
        ordering = ['-uploaded_at']
        verbose_name = 'Image Processing'
        verbose_name_plural = 'Images Processing'

    def save(self, *args, **kwargs):
        # Générer un nom unique si le champ `name` est vide
        if not self.name:
            self.name = str(uuid.uuid4())  # Génère un UUID unique comme nom
        super().save(*args, **kwargs)

    def clean(self):
        # Validation de la taille de l'image
        if self.original_image.size > 5 * 1024 * 1024:  # 5 Mo en octets
            raise ValidationError("La taille de l'image ne doit pas dépasser 5 Mo.")
