from django.conf.urls import url
from django.urls import path

from .views import *
from products.views import product

urlpatterns = [
    # url(r'^$', landing, name='landing.html'),
    url(r'^$', home, name='base.html'),
    url(r'^product/(?P<product_id>\d+)$', product, name='product.html'),

]
