# Generated by Django 2.0 on 2017-12-14 08:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_auto_20171214_1131'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='productimage',
            name='description',
        ),
        migrations.RemoveField(
            model_name='productimage',
            name='total_cost',
        ),
    ]
