# Generated by Django 4.1.2 on 2023-03-30 03:34

from django.db import migrations, models
import django.db.models.deletion
import mdeditor.fields


class Migration(migrations.Migration):

    dependencies = [
        ('featuress', '0005_alter_benefitfeatures_thumbnail_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Feature',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('thumbnail', models.ImageField(blank=True, null=True, upload_to='image')),
            ],
            options={
                'verbose_name': 'Feature',
                'verbose_name_plural': 'Features',
            },
        ),
        migrations.CreateModel(
            name='SubFeature',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('desc', mdeditor.fields.MDTextField()),
                ('thumbnail', models.ImageField(blank=True, null=True, upload_to='image')),
                ('sub_title', models.CharField(max_length=255)),
                ('content', mdeditor.fields.MDTextField()),
                ('feature_slug', models.SlugField(blank=True, max_length=255, null=True)),
                ('SubFeature_slug', models.SlugField(blank=True, max_length=255, null=True)),
                ('feature', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='featuress.feature')),
            ],
            options={
                'verbose_name': 'SubFeature',
                'verbose_name_plural': 'SubFeatures',
            },
        ),
        migrations.RemoveField(
            model_name='subfeatures',
            name='features',
        ),
        migrations.DeleteModel(
            name='BenefitFeatures',
        ),
        migrations.DeleteModel(
            name='Features',
        ),
        migrations.DeleteModel(
            name='SubFeatures',
        ),
    ]