from django.conf.urls import url
from tickets.views import create_ticket, show_ticket

urlpatterns = [
    url(r'^ticket/create', create_ticket, name="create_ticket"),
    url(r'^ticket/', show_ticket, name="read_ticket")
]
