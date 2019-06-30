from django.conf.urls import url
from voteshop.views import checkout, buyvotes, success, fail

urlpatterns = [
    url(r'^checkout', checkout, name='checkout'),
    url(r'^$', buyvotes, name='buyvotes'),
    url(r'^success', success, name='success'),
    url(r'^fail', fail, name='fail'),

]
