# Generated by Django 2.0 on 2017-12-18 02:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_auto_20171218_0526'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='cost',
        ),
    ]
