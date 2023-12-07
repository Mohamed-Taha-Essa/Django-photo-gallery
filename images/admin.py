from django.contrib import admin
from .models import Album,Photo
from django.utils.safestring import mark_safe

# Register your models here.

class AlbumModel(admin.ModelAdmin):
    list_display=['title','user']

admin.site.register(Album,AlbumModel)


class PhotoModel(admin.ModelAdmin):
    list_display = ['display_title', 'display_image', 'alt_text']

    def display_image(self, obj):
        if obj.image:
            return mark_safe('<img src="{}" style="max-width: 100px; max-height: 100px;" />'.format(obj.image.url))
        return '-'
    display_image.short_description = 'Image Preview'

    def display_title(self, obj):
        return obj.album
    display_title.short_description = 'Title'

admin.site.register(Photo, PhotoModel)