# Generated by Django 2.0 on 2017-12-18 02:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='total_cost',
            new_name='cost',
        ),
        migrations.RemoveField(
            model_name='productimage',
            name='description',
        ),
        migrations.RemoveField(
            model_name='productimage',
            name='total_cost',
        ),
        migrations.AlterField(
            model_name='productimage',
            name='image',
            field=models.ImageField(upload_to='images/product_images/%Y/%m/%d', verbose_name='Фото товара'),
        ),
    ]
