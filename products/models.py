from django.db import models
from django.utils.html import format_html


class Product(models.Model):
    name = models.CharField(max_length=128)
    description = models.TextField(blank=True)
    created = models.DateTimeField(auto_now_add=True)
    cost = models.DecimalField(max_digits=9, decimal_places=2)

    def __str__(self):
        return "{}".format(self.name)

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = "Товары"


class ProductImage(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    image = models.ImageField(upload_to="images/product_images/%Y/%m/%d", verbose_name='Фото товара')
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "Картинка для товара: {}".format(self.product.name)

    def image_img(self):
        if self.image:
            return format_html(r'<a href="{0}" target="_blank"><img src="{0}" width="50"/></a>'.format(
                self.image.url))
        else:
            return '(Нет изображения)'
    image_img.short_description = 'image'

    class Meta:
        verbose_name = 'Картинка'
        verbose_name_plural = "Картинки"
