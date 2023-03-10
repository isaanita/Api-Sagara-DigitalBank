from django.db import models
from mdeditor.fields import MDTextField
from slugify import slugify
from django.utils.translation import gettext_lazy as _

# Create your models here.

# Features Models
class features(models.Model):
    features_tittle = models.CharField(max_length=255)
    thumbnail = models.ImageField(upload_to='image')
    description = MDTextField(default='', null=False)

    content_tittle = models.CharField(max_length=255)
    content_thumbnail = models.ImageField(upload_to='image')
    content_description = MDTextField(default='', null=False)
    

    features_slug = models.SlugField(max_length=255, blank=True, default='')

    def save(self, *args, **kwargs):
        self.features_slug = slugify(self.feature_title)
        return super().save(*args, **kwargs)

    class Meta:
        verbose_name = _("Feature")
        verbose_name_plural = _("features")