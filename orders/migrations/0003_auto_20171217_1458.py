# Generated by Django 2.0 on 2017-12-17 11:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0002_auto_20171217_0023'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='order',
            options={},
        ),
        migrations.AlterModelOptions(
            name='productinorder',
            options={'verbose_name': 'Product', 'verbose_name_plural': 'Products'},
        ),
        migrations.AlterModelOptions(
            name='status',
            options={'verbose_name': 'Order status', 'verbose_name_plural': 'Order statuses'},
        ),
    ]
