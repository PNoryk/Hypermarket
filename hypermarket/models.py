from django.db import models
from django.utils import timezone


# Create your models here.


class Product(models.Model):
    title = models.CharField(max_length=255, help_text="Input title text")
    text = models.TextField()
    created_date = models.DateTimeField(
        default=timezone.now)
    published_date = models.DateTimeField(
        blank=True, null=True)
    picture = models.ImageField(default="images/NoPicAvailable.png",
                                upload_to="images/%Y/%m/%d", verbose_name='Ссылка картинки',
                                )

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title

    def img(self):
        return self.picture.path
