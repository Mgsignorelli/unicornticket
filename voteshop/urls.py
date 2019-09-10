from django.conf.urls import url
from voteshop.views import buyvotes, success, fail

# Buy votes urls

urlpatterns = [
    url(r'^$', buyvotes, name='buyvotes'),
    url(r'^success/(?P<order_id>[0-9]+)', success, name='success'),
    url(r'^fail/(?P<order_id>[0-9]+)', fail, name='fail'),

]
