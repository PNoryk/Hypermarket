# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-12 22:27
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hypermarket', '0006_auto_20171213_0120'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='picture',
            field=models.ImageField(default='settings.MEDIA_ROOT/images/NoPicAvailable.png', upload_to='images/%Y/%m/%d', verbose_name='Ссылка картинки'),
        ),
    ]
