from django.db import models
from django.db.models.signals import post_save
from decimal import *
from django.dispatch import receiver

from customer.models import Customer
from products.models import Product


class Status(models.Model):
    name = models.CharField(max_length=25, default="New")

    # def __init__(self, name, *args, **kwargs):
    #     self.name = name
    #     super().__init__(*args, **kwargs)

    def __str__(self):
        return "{}".format(self.name)

    class Meta:
        verbose_name = 'Order status'
        verbose_name_plural = "Order statuses"


class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.DO_NOTHING)
    comments = models.TextField(blank=True)
    status = models.ForeignKey(Status, on_delete=models.DO_NOTHING, default="New")
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    order_total_price = models.DecimalField(max_digits=9, decimal_places=2, default=0)

    def __str__(self):
        return "Order: {}, status: {}".format(self.id, self.status.name)

    # class Meta:
    #     verbose_name = 'Order'
    #     verbose_name_plural = "Orders"

    def save(self, *args, **kwargs):
        super(Order, self).save(*args, **kwargs)


class ProductInOrder(models.Model):
    order = models.ForeignKey(Order, on_delete=models.DO_NOTHING)
    product = models.ForeignKey(Product, on_delete=models.DO_NOTHING)
    count = models.IntegerField(default=1)
    price_per_item = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    product_total_price = models.DecimalField(max_digits=10, decimal_places=2, default=0,
                                              verbose_name='total price')  # price*nmb
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __str__(self):
        return "{}".format(self.product.name)

    class Meta:
        verbose_name = 'Product in order'
        verbose_name_plural = "Products in order"

    def save(self, *args, **kwargs):
        prod = Product.objects.filter(name=self.product)[0]
        # a = models.DecimalField(round(prod.price - prod.discount / 100 * prod.price), 2)
        # self.price_per_item = (prod.price * 0.01)
        self.price_per_item = prod.price - prod.discount / Decimal(100) * prod.price
        # self.product_per_item = Decimal(self.product.price * 0.01).quantize(Decimal("1.00"))
        self.product_total_price = self.count * self.price_per_item
        super(ProductInOrder, self).save(*args, **kwargs)


@receiver(post_save, sender=ProductInOrder)
def product_in_order_post_save(instance, **kwargs):
    order = instance.order
    all_products_in_order = ProductInOrder.objects.filter(order=order)

    order_total_price = 0
    for item in all_products_in_order:
        order_total_price += item.product_total_price

    order.order_total_price = order_total_price
    order.save(force_update=True)
