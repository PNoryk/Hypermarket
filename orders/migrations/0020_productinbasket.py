# Generated by Django 2.0 on 2017-12-19 15:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0010_auto_20171218_2340'),
        ('orders', '0019_auto_20171218_2338'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProductInBasket',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('count', models.IntegerField(default=1)),
                ('price_per_item', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
                ('product_total_price', models.DecimalField(decimal_places=2, default=0, max_digits=10, verbose_name='total price')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='orders.Order')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='products.Product')),
            ],
            options={
                'verbose_name': 'Product in basket',
                'verbose_name_plural': 'Products in Basket',
            },
        ),
    ]