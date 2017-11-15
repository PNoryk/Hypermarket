from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.product_list, name='product_list'),
url(r'^post/(?P<pk>\d+)/$', views.post_detail, name='post_detail'),
]