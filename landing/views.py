from django.shortcuts import render

# Create your views here.
from products.models import Product,ProductImage


def landing(request):
    return render(request, "landing/landing.html", locals())


def home(request):
    products_images = ProductImage.objects.filter(is_main=True)
    products_images_hleb = ProductImage.objects.filter(product__category__name='Хлеб', is_main=True)
    products_images_test = ProductImage.objects.filter(product__category__name='ТЕСТ', is_main=True)

    return render(request, 'landing/home.html', locals())
