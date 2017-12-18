from django.shortcuts import render

# Create your views here.
from products.models import Product,ProductImage


def landing(request):
    return render(request, "landing/home.html", locals())


def home(request):
    products = Product.objects.filter()
    products_images = ProductImage.objects.filter(is_main=True)
    return render(request, 'landing/home.html', locals())
