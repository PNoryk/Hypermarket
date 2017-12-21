from django.http import JsonResponse
from django.shortcuts import render

from products.models import ProductImage
from .models import *


# Create your views here.

def basket_adding(request):
    return_dict = dict()
    session_key = request.session.session_key

    data = request.POST
    product_id = data.get('product_id')
    count = data.get('product_count')
    is_delete = data.get("is_delete")

    if is_delete == 'true':
        deleted_products = ProductInBasket.objects.filter(id=product_id)
        for item in deleted_products:
            item.delete()
    else:
        new_product, created = ProductInBasket.objects.get_or_create(session_key=session_key, product_id=product_id,
                                                                     defaults={'count': count})
        if not created:
            new_product.count += int(count)
            new_product.save(force_update=True)

    products_in_basket = ProductInBasket.objects.filter(session_key=session_key)
    products_total_number = products_in_basket.count()
    return_dict["products_total_number"] = products_total_number

    return_dict["products"] = list()

    for item in products_in_basket:
        product_dict = dict()
        product_dict["id"] = item.id
        product_dict["name"] = item.product.name
        product_dict["price_per_item"] = item.price_per_item
        product_dict["count"] = item.count
        product_dict["product_total_price"] = item.product_total_price

        return_dict["products"].append(product_dict)

    return JsonResponse(return_dict)


def basket(request):
    session_key = request.session.session_key

    prod_with_picture = dict()
    products_in_basket = ProductInBasket.objects.filter(session_key=session_key)
    products_images = ProductImage.objects.filter(is_main=True)
    for i in range(len(products_in_basket)):
        prod_with_picture = {products_in_basket[i].product.name: products_images[i].image}

    return render(request, 'orders/basket.html', locals())
