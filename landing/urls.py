from django.conf.urls import url

from .views import *

urlpatterns = [
    # url(r'^$', landing, name='landing.html'),
    url(r'^$', home, name='base.html'),

]
