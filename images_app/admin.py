from django.contrib import admin
from .models import ImageProcessing


@admin.register(ImageProcessing)
class ImageProcessingAdmin(admin.ModelAdmin):
    list_display = ['name', 'original_image', 'processed_image', 'background_color', 'uploaded_at', 'ip_address']
    list_filter = ['uploaded_at']
    search_fields = ['name', 'background_color']
    list_per_page = 10
    date_hierarchy = 'uploaded_at'
    readonly_fields = ['uploaded_at', 'ip_address']
    fieldsets = [
        ('Image Info', {'fields': ['name', 'original_image', 'processed_image', 'background_color']}),
        ('Meta Info', {'fields': ['uploaded_at', 'ip_address']}),
    ]
 

