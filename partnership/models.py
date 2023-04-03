from django.db import models
from mdeditor.fields import MDTextField
from django.utils.translation import gettext_lazy as _
from slugify import slugify

# Create your models here.

# Category Partnership
class CategoryPartner(models.Model):
    partner_type = models.CharField(max_length=255)
    region_type = models.CharField(max_length=255)
    solution_type = models.CharField(max_length=255)

    class Meta:
        verbose_name = _("CategoryPartner")
        verbose_name_plural = _("CategoryPartners")

class ContentPartner(models.Model):
    thumbnail = models.ImageField(upload_to="image", blank=True, null=True)
    desc = MDTextField()

    categoryPartner = models.ForeignKey(CategoryPartner, on_delete=models.DO_NOTHING)

    categoryPartner_slug = models.SlugField(max_length=255, blank=True, null=True)
    contentPartner_slug = models.SlugField(max_length=255, blank=True, null=True)

    def save(self, *args, **kwargs):
        self.categoryPartner_slug = slugify(self.categoryPartner.partner_type)
        self.contentPartner_slug = slugify(self.desc)
        return super().save(*args, **kwargs)
    
    class Meta:
        verbose_name = _("Partner")
        verbose_name_plural = _("Partners")