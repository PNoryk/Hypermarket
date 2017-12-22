from django.shortcuts import render

# Create your views here.
from products.models import Product, ProductImage, ProductCategory


def landing(request):
    return render(request, "landing/landing.html", locals())


def home(request):
    products_images = ProductImage.objects.filter(is_main=True)

    product_categories = ProductCategory.objects.all()

    # product_images_by_category = []
    # for category in product_categories:
    #     product_images_by_category.append(ProductImage.objects.filter(product__category=category, is_main=True))

    if request.POST:
        category = request.POST.get('select-category')
        print(category)
        selected_category_products = ProductImage.objects.filter(product__category__name=category, is_main=True)
        print(selected_category_products[0])
        # selected_category_products = selected_category_products[0].objects.all()

    return render(request, 'landing/home.html', locals())
