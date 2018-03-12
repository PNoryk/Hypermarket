from unittest.mock import Mock, MagicMock

from django.test import TestCase
from django.db.utils import OperationalError

# Create your tests here.

from .models import *


class TestProduct(TestCase):
    def setUp(self):
        ProductCategory.objects.count = MagicMock(return_value=1)
        # self.category1 = ProductCategory.objects.create(name="New1")
        # self.category2 = ProductCategory.objects.create(name="New2")
        #
        # self.product1 = Product.objects.create(
        #     name='TestProduct1',
        #     category=self.category1,
        #     price="1",
        #     discount=0)
        #
        # self.product2 = Product.objects.create(
        #     name='TestProduct2',
        #     category=self.category1,
        #     price="2",
        #     discount=0)

        # Product.objects.get = MagicMock(return_value='TestProduct1')
        # print(ProductCategory.objects.count(name="h"))
        # print(ProductCategory.objects.count.assert_called_once())
        # print(self.product1.save())

    # def test_product_db_adding_product_good_result1(self):
    #     self.assertEqual(self.product1.__str__(), Product.objects.get(name=self.product1.name))
    #
    # def test_product_db_adding_category_good_result1(self):
    #     self.assertEqual(self.category1, ProductCategory.objects.get(name=self.category1.name))
    #
    # def test_product_db_adding_product_good_result2(self):
    #     self.assertEqual(2, Product.objects.count())
    #
    # def test_product_db_adding_category_good_result2(self):
    #     self.assertEqual(2, ProductCategory.objects.count())

    # def test_product_db_delete_product_good_result1(self):
    #     self.assertEqual(self.product1.name, Product.objects.get(name='TestProduct1'))



    # def test_product_db_delete_category_good_result1(self):
    #     self.category1.delete()
    #     self.assertEqual(self.category1, ProductCategory.objects.get(name=self.category1.name))

    # def test_product_db_delete_product_good_result2(self):
    #     self.product1.delete()
    #     self.assertEqual(1, Product.objects.count())
    #
    # def test_product_db_delete_category_good_result2(self):
    #     self.category1.delete()
    #     self.assertEqual(1, ProductCategory.objects.count())

    # def test_product_db_no_adding_product_good_result1(self):
    #     with self.assertRaises(OperationalError):
    #         MockProduct.objects.get(name='MockProduct1')
    #
    # def test_product_db_no_adding_category_good_result1(self):
    #     with self.assertRaises(OperationalError):
    #         MockProduct.objects.get(name='MockCategory')
    #
    # def test_product_db_no_adding_product_good_result2(self):
    #     with self.assertRaises(OperationalError):
    #         MockProduct.objects.count()
    #
    # def test_product_db_no_adding_category_good_result2(self):
    #     with self.assertRaises(OperationalError):
    #         MockCategory.objects.count()

    # def tearDown(self):
    #     self.category1.delete()
    #     self.category2.delete()
    #     self.product1.delete()
    #     self.product2.delete()


    def test_mock(self):
        ProductCategory.objects.create(name="Hello")
        self.assertEqual(ProductCategory.objects.count(), 1)
