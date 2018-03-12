from django.core.validators import validate_slug
from django.db import models
from mysite.settings import MEDIA_URL

from django.utils.html import format_html
# from imagekit.models.fields import ImageSpecField
# from imagekit.processors import ResizeToFit, Adjust,ResizeToFill


class Customer(models.Model):
    name = models.CharField(max_length=255, validators=[validate_slug])
    phone = models.DecimalField(max_digits=9, decimal_places=0)
    address = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    avatar = models.ImageField(upload_to="images/avatars/%Y/%m/%d", blank=True)
    # avatar_thumbnail = ImageSpecField(source='avatar',
    #                                   processors=[ResizeToFill(50, 50)],
    #                                   format='JPEG',
    #                                   options={'quality': 60})

    def __str__(self):
        return "Customer: {}".format(self.name)

    def image_img(self):
        if self.avatar and self.avatar.isatty:
            return format_html(r'<a href="{0}" target="_blank"><img src="{0}" width="50"/></a>'.format(
                self.avatar.url))
        else:
            return format_html(r'<a href="{0}" target="_blank"><img src="{0}" width="50"/></a>'.format(
                MEDIA_URL + "images/NoPictureAvailable.png"))

    image_img.allow_tags = True
    image_img.short_description = 'Avatar'

    # class Meta:
    #     verbose_name = 'Customer'
    #     verbose_name_plural = "Customers"

