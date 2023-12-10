from django.contrib import admin
from .models import Album,Photo
from django.utils.safestring import mark_safe

# Register your models here.

class AlbumModel(admin.ModelAdmin):
    list_display=['title','display_image','user']

admin.site.register(Album,AlbumModel)


class PhotoModel(admin.ModelAdmin):
    list_display = ['display_title', 'display_image', 'alt_text']

    def display_title(self, obj):
        return obj.album
    display_title.short_description = 'Title'

admin.site.register(Photo, PhotoModel)