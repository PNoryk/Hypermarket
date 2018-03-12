from django.test import TestCase
from .models import *
from customer.models import Customer
from products.models import Product, ProductCategory


class TestProductInOrder(TestCase):

    def setUp(self):
        self.customer = Customer.objects.create(
            name='Pavel',
            phone=123,
            address='Doroshevicha 3')
        self.status = Status.objects.create()
        self.order = Order.objects.create(
            customer=self.customer,
            comments='12e',
            status=self.status
        )
        self.category = ProductCategory.objects.create(name='New')
        self.product = Product.objects.create(
            name="hello",
            description='description',
            category=self.category,
            price=10,
            discount=0
        )
        self.product2 = Product.objects.create(
            name="prod2",
            description='description',
            category=self.category,
            price=10,
            discount=10
        )
        self.prod_in_oredr = ProductInOrder.objects.create(
            order=self.order,
            product=self.product)

    def test_set_product_discount_good_data_return_true(self):
        product_in_order = ProductInOrder.objects.filter(product_id=self.product.id)
        self.assertEqual(int(product_in_order[0].product_total_price),
                         self.product.price - self.product.price * self.product.discount * 0.01)

    def test_product_price_in_order_price_good_data_return_true(self):
        product_in_order = ProductInOrder.objects.get(product_id=self.product.id)
        count = product_in_order.count
        self.assertEqual(product_in_order.product_total_price, count * product_in_order.price_per_item)


class TestProductInOrderPostSave(TestCase):
    def setUp(self):
        self.customer = Customer.objects.create(
            name='Pavel',
            phone=123,
            address='Doroshevicha 3')
        self.status = Status.objects.create()
        self.order = Order.objects.create(
            customer=self.customer,
            comments='12e',
            status=self.status
        )
        self.category = ProductCategory.objects.create(name='New')
        self.product = Product.objects.create(
            name="hello",
            description='description',
            category=self.category,
            price=10,
            discount=0
        )
        self.product2 = Product.objects.create(
            name="prod2",
            description='description',
            category=self.category,
            price=10,
            discount=10
        )
        self.prod_in_oredr = ProductInOrder.objects.create(
            order=self.order,
            product=self.product)

    def test_product_in_order_post_save_add_product_good_data_return_true(self):
        self.assertEqual(self.order.order_total_price, self.product.price)

    def test_product_in_order_post_save_add_2_product_good_data_return_true(self):
        ProductInOrder.objects.create(order=self.order,
                                      product=self.product2)
        self.assertEqual(self.order.order_total_price, 19)
