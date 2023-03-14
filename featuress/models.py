from django.db import models
from mdeditor.fields import MDTextField
from django.utils.translation import gettext_lazy as _
from slugify import slugify

# Create your models here.

# Features Models
class Features(models.Model):
    features_title = models.CharField(max_length=255)
    features_desc = MDTextField()
    feature_thumbnail = models.ImageField(upload_to='image', blank=True, null=True)
    category = models.CharField(max_length=255, default='')

    class Meta:
        verbose_name = _("Feature")
        verbose_name_plural = _("Features")

# Sub Features Models
class SubFeatures(models.Model):
    features = models.ForeignKey(Features, on_delete=models.DO_NOTHING)
    sub_features_title = models.CharField(max_length=255)
    sub_features_desc = MDTextField()

    features_slug = models.SlugField(max_length=255, blank=True, null=True)
    sub_features_slug = models.SlugField(max_length=255, blank=True, null=True)

    def save(self, *args, **kwargs):
        self.features_slug = slugify(self.features.features_title)
        self.sub_features_slug = slugify(self.sub_features_title)
        return super().save(*args, **kwargs)
    
    class Meta:
        verbose_name = _("SubFeature")
        verbose_name_plural = _("SubFeatures")
    
# Benfit Features
class BenefitFeatures(models.Model):
    sub_features = models.ForeignKey(SubFeatures, on_delete=models.DO_NOTHING)
    thumbnail = models.ImageField(upload_to='image', blank=True, null=True)
    title = models.CharField(max_length=255)
    desc = MDTextField()

    sub_features_slug = models.SlugField(max_length=255, blank=True, null=True)
    benefit_features_slug = models.SlugField(max_length=255, blank=True, null=True)

    def save(self, *args, **kwargs):
        self.sub_features_slug = slugify(self.sub_features.sub_features_title)
        self.benefit_features_slug = slugify(self.title)
        return super().save(*args, **kwargs)
    
    class Meta:
        verbose_name = _("BenefitFeature")
        verbose_name_plural = _("BenefitFeatures")