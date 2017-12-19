# Generated by Django 2.0 on 2017-12-18 04:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0016_auto_20171218_0702'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='productinorder',
            options={'verbose_name': 'Product in order', 'verbose_name_plural': 'Products in order'},
        ),
        migrations.AddField(
            model_name='order',
            name='updated',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='status',
            name='updated',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
