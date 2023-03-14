from django.db import models
from mdeditor.fields import MDTextField
from django.utils.translation import gettext_lazy as _
from slugify import slugify

# Create your models here.

class Partnering(models.Model):
    title = models.CharField(max_length=255)
    desc = MDTextField()
    thumbnail = models.ImageField(upload_to='image', blank=True, null=True)
    content = models.CharField(max_length=255)

class Partner(models.Model):
    thumbnail = models.ImageField(upload_to='image', blank=True, null=True)
    desc = MDTextField()