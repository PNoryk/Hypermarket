from django.conf.urls import url

from products.views import product

urlpatterns = [
    url(r'^product/(?P<product_id>\w+)$', product, name='product'),


]
