from django import forms
from pip.cmdoptions import verbose

from .models import Product


class PostForm(forms.ModelForm):

    class Meta:
        verbose_name = "Продукт"
        verbose_name_plural = "Продукты"

        model = Product
        fields = ('title', 'text', 'picture')
