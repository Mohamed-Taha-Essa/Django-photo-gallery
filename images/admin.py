from django.contrib import admin
from .models import Album,Photo
from django.utils.html import format_html

# Register your models here.

class AlbumModel(admin.ModelAdmin):
    list_display=['title','user']

admin.site.register(Album,AlbumModel)


class PhotoModel(admin.ModelAdmin):
    list_display = ['display_title', 'display_image', 'alt_text']

    def display_image(self, obj):
        return format_html('<img src="{}" style="max-width: 100px; max-height: 100px;" />',
                           obj.image.url) if obj.image else '-'
    display_image.short_description = 'Image Preview'
    
    def display_title(self, obj):
        return obj.album
    display_title.short_description = 'Title'

admin.site.register(Photo, PhotoModel)