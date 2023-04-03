from django.db import models
from mdeditor.fields import MDTextField
from django.utils.translation import gettext_lazy as _
from slugify import slugify

# Create your models here.

# Features Models
class Feature(models.Model):
    title = models.CharField(max_length=255)
    thumbnail = models.ImageField(upload_to='image', blank=True, null=True)

    class Meta:
        verbose_name = _("Feature")
        verbose_name_plural = _("Features")

# Sub Features Models
class SubFeature(models.Model):
    title = models.CharField(max_length=255)
    desc = MDTextField()
    thumbnail = models.ImageField(upload_to='image', blank=True, null=True)
    sub_title = models.CharField(max_length=255)
    content = MDTextField()

    feature = models.ForeignKey(Feature, on_delete=models.DO_NOTHING)

    feature_slug = models.SlugField(max_length=255, blank=True, null=True)
    SubFeature_slug = models.SlugField(max_length=255, blank=True, null=True)

    def save(self, *args, **kwargs):
        self.feature_slug = slugify(self.feature.title)
        self.SubFeature_slug = slugify(self.title)
        return super().save(*args, **kwargs)
    class Meta:
        verbose_name = _("SubFeature")
        verbose_name_plural = _("SubFeatures")
