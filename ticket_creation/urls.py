from django.conf.urls import url, include
from ticket_creation.views import create_ticket


urlpatterns = [
    url(r'^create_ticket/', create_ticket, name="create_ticket")
]