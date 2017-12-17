from django.db import models
from django.utils import timezone


# Create your models here.
from django.utils.html import format_html


class Product(models.Model):
    title = models.CharField(max_length=255, help_text="Input title text")
    text = models.TextField()
    created_date = models.DateTimeField(
        default=timezone.now)
    published_date = models.DateTimeField(
        blank=True, null=True)
    picture = models.ImageField(default="images/NoPicAvailable.png",
                                upload_to="images/%Y/%m/%d", verbose_name='Ссылка картинки')

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title

    def image_img(self):
        if self.picture:
            return format_html(r'<a href="{0}" target="_blank"><img src="{0}" width="100"/></a>'.format(
                self.picture.url))
        else:
            return '(Нет изображения)'

    image_img.allow_tags = True
    image_img.short_description = 'Картинка'

