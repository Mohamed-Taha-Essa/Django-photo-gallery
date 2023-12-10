from django.db import models
from django.contrib.auth.models import User
from django.utils.safestring import mark_safe

# Create your models here.


class Album(models.Model):
    image = models.ImageField(upload_to='album_img/' ,null=True)
    user = models.ForeignKey(User ,related_name='album_user' ,on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    
    def __str__(self):
        return self.title
    
    def display_image(self):
        return mark_safe('<img src="%s" width="100" />'%(self.image.url))
    


class Photo(models.Model):
    album = models.ForeignKey(Album ,related_name='photo_album' ,on_delete=models.CASCADE)
    image = models.ImageField(upload_to='photos/')
    alt_text = models.CharField(max_length=100)

    def display_image(self):
        return mark_safe('<img src="{}" style="max-width: 100px; max-height: 100px;" />'.format(self.image.url))

    def __str__(self):
        return self.alt_text
    