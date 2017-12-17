from django.db import models

from customer.models import Customer
from products.models import Product


class Status(models.Model):
    name = models.CharField(max_length=25)

    def __str__(self):
        return "Status: {}".format(self.name)

    class Meta:
        verbose_name = 'Order status'
        verbose_name_plural = "Order statuses"


class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.DO_NOTHING)
    comments = models.TextField(blank=True)
    status = models.ForeignKey(Status, blank=True, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    total_cost = models.DecimalField(max_digits=9, decimal_places=2)

    def __str__(self):
        return "Order: {}, status: {}".format(self.id, self.status.name)

    # class Meta:
    #     verbose_name = 'Order'
    #     verbose_name_plural = "Orders"


class ProductInOrder(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)

    def __str__(self):
        return "{}".format(self.product.name)

    class Meta:
        verbose_name = 'Product'
        verbose_name_plural = "Products"
