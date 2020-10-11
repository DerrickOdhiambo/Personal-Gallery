from django.db import models


class Image(models.Model):
    image = models.ImageField(upload_to='index/')
    image_name = models.CharField(max_length=100)
    image_description = models.TextField()
