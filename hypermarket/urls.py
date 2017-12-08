from django.conf import settings
from django.conf.urls import url
from django.conf.urls.static import static
from . import views
from django.views.generic import DetailView
from .models import Product

urlpatterns = [
    url(r'^$', views.product_list, name='product_list'),
    url(r'^post/(?P<pk>\d+)/$', views.post_detail, name='post_detail'),
    url(r'^post/new/$', views.post_new, name='post_new'),
    # url(r'^post/(?P<pk>[0-9]+)/$', DetailView.as_view(
    #     context_object_name="Product",
    #     model=Product,
    #     template_name="post_list.html"
    # ), name='')
]
