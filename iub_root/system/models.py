from django.db import models


# Create your models here.
class Image_Data(models.Model):
    image = models.ImageField(upload_to="media")
