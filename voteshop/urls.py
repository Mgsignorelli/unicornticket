from django.conf.urls import url
from voteshop.views import checkout, buyvotes

urlpatterns = [
    url(r'^checkout', checkout, name='checkout'),
    url(r'^$', buyvotes, name='buyvotes'),
]
