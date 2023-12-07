from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Album(models.Model):
    user = models.ForeignKey(User ,related_name='album_user' ,on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    
    def __str__(self):
        return self.title
    


class Photo(models.Model):
    album = models.ForeignKey(Album ,related_name='photo_album' ,on_delete=models.CASCADE)
    image = models.ImageField(upload_to='photos/')
    alt_text = models.CharField(max_length=100)

    def __str__(self):
        return self.alt_text
    