from django.db import models
from django.utils.html import format_html


class ProductCategory(models.Model):
    name = models.CharField(max_length=64, blank=True, null=True, default=None)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return "{}".format(self.name)

    class Meta:
        verbose_name = 'Product category'
        verbose_name_plural = 'Product categories'


class Product(models.Model):
    name = models.CharField(max_length=128)
    description = models.TextField(blank=True)
    category = models.ForeignKey(ProductCategory, on_delete=models.DO_NOTHING, blank=True, null=True, default=None)
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "{}".format(self.name)

    # class Meta:
    #     verbose_name = 'Product'
    #     verbose_name_plural = "Products"


class ProductImage(models.Model):
    product = models.ForeignKey(Product, on_delete=models.DO_NOTHING)
    image = models.ImageField(upload_to="images/product_images/%Y/%m/%d")
    is_main = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "Image to: {}".format(self.product.name)

    def image_img(self):
        if self.image:
            return format_html(r'<a href="{0}" target="_blank"><img src="{0}" width="50"/></a>'.format(
                self.image.url))
        else:
            return '(No image)'

    image_img.short_description = 'image'

    class Meta:
        verbose_name = 'Product image'
        verbose_name_plural = "Product images"
