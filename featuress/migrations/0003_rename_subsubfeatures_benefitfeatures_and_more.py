# Generated by Django 4.1.2 on 2023-03-13 09:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('featuress', '0002_remove_features_category_slug_and_more'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='SubSubFeatures',
            new_name='BenefitFeatures',
        ),
        migrations.RenameField(
            model_name='subfeatures',
            old_name='fetures_slug',
            new_name='features_slug',
        ),
    ]
