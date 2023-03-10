from django.db import models
from mdeditor.fields import MDTextField
from slugify import slugify
from django.utils.translation import gettext_lazy as _

class solution(models.Model):
    solution_title = models.CharField(max_length=155)
    description = MDTextField(default='', null=False)

    solution_slug = models.SlugField(max_length=255, blank=True, default='')

    def save(self, *args, **kwargs):
        self.solution_slug = slugify(self.solution_title)
        return super().save(*args, **kwargs)
    
    class Meta:
        verbose_name = _("Solution")
        verbose_name_plural = _("solution")
