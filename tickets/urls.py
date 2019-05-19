from django.conf.urls import url
from tickets.views import create_ticket, read_ticket

urlpatterns = [
    url(r'^ticket/create', create_ticket, name="create_ticket"),
    url(r'^ticket/', read_ticket, name="read_ticket")
]
