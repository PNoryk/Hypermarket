from django.shortcuts import render

# Create your views here.
from products.models import ProductImage, ProductCategory


def landing(request):
    return render(request, "landing/landing.html")


def home(request):
    products_images = ProductImage.objects.filter(is_main=True)
    product_categories = ProductCategory.objects.all()

    if request.POST:
        category = request.POST.get('select-category')
        selected_category_products = ProductImage.objects.filter(product__category__name=category, is_main=True)

    return render(request, 'landing/home.html', locals())
