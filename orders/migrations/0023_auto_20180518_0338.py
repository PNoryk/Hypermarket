# Generated by Django 2.0.3 on 2018-05-18 00:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0022_auto_20171219_1956'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productinorder',
            name='count',
            field=models.PositiveIntegerField(default=1),
        ),
    ]