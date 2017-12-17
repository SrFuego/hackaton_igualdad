# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2017-12-17 04:19
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import model_utils.fields
import stdimage.models
import stdimage.utils
import stdimage.validators


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Package',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('name', models.CharField(max_length=50)),
                ('description', models.TextField()),
                ('price', models.PositiveSmallIntegerField()),
                ('time', models.CharField(max_length=50)),
            ],
            options={
                'verbose_name': 'Paquete',
            },
        ),
        migrations.CreateModel(
            name='PackageImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', stdimage.models.StdImageField(upload_to=stdimage.utils.UploadToAutoSlugClassNameDir('package.name'), validators=[stdimage.validators.MinSizeValidator(400, 250), stdimage.validators.MaxSizeValidator(1000, 1000)])),
                ('package', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='packages.Package')),
            ],
            options={
                'verbose_name': 'Imagen',
                'verbose_name_plural': 'Imagenes',
            },
        ),
    ]
