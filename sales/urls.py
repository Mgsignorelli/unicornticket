from django.conf.urls import url
from sales.views import app_home

urlpatterns = [
    url(r'^app_home', app_home, name="app_home")
]
