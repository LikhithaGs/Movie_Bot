from django.db import models
from django.views.generic import TemplateView

# Create your models here.

class Movie(models.Model):
    movie_title = models.CharField(max_length=100)
    movie_details = models.TextField()
    movie_card = models.ImageField(upload_to='movie')

class Main(models.Model):
    main_img = models.ImageField(upload_to='movie')
