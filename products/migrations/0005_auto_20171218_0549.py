# Generated by Django 2.0 on 2017-12-18 02:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_product_cost'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='product',
            options={},
        ),
        migrations.AlterModelOptions(
            name='productimage',
            options={'verbose_name': 'Product image', 'verbose_name_plural': 'Product images'},
        ),
        migrations.RenameField(
            model_name='product',
            old_name='cost',
            new_name='price',
        ),
        migrations.AlterField(
            model_name='productimage',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='products.Product'),
        ),
    ]
