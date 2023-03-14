# Generated by Django 4.1.2 on 2023-03-14 03:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('featuress', '0003_rename_subsubfeatures_benefitfeatures_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='benefitfeatures',
            options={'verbose_name': 'BenefitFeature', 'verbose_name_plural': 'BenefitFeatures'},
        ),
        migrations.AlterModelOptions(
            name='features',
            options={'verbose_name': 'Feature', 'verbose_name_plural': 'Features'},
        ),
        migrations.AlterModelOptions(
            name='subfeatures',
            options={'verbose_name': 'SubFeature', 'verbose_name_plural': 'SubFeatures'},
        ),
        migrations.RenameField(
            model_name='benefitfeatures',
            old_name='relation',
            new_name='sub_features',
        ),
        migrations.RenameField(
            model_name='subfeatures',
            old_name='relation',
            new_name='features',
        ),
        migrations.RemoveField(
            model_name='benefitfeatures',
            name='sub_features_titles',
        ),
        migrations.RemoveField(
            model_name='features',
            name='slug',
        ),
        migrations.RemoveField(
            model_name='subfeatures',
            name='features_titles',
        ),
        migrations.AddField(
            model_name='benefitfeatures',
            name='benefit_features_slug',
            field=models.SlugField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='benefitfeatures',
            name='sub_features_slug',
            field=models.SlugField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='subfeatures',
            name='features_slug',
            field=models.SlugField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='subfeatures',
            name='sub_features_slug',
            field=models.SlugField(blank=True, max_length=255, null=True),
        ),
    ]