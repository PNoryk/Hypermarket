from django.db import models
from django.utils import timezone


# Create your models here.


class Product(models.Model):
    author = models.ForeignKey('auth.User')
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(
        default=timezone.now)
    published_date = models.DateTimeField(
        blank=True, null=True)
    picture = models.ImageField(default=r"file////C:/Users/MSI-PNoryk/Desktop/site/NoPicAvailable.png",
                                upload_to="images/%Y/%m/%d", verbose_name='Ссылка картинки')

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title

    def img(self):
        return self.picture.path
