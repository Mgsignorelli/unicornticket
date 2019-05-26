from django.conf.urls import url
from tickets.views import create_ticket, show_bug, show_feature

urlpatterns = [
    url(r'^ticket/create', create_ticket, name="create_ticket"),
    url(r'^bug/(?P<id>[0-9]+)', show_bug, name="show_bug"),
    url(r'^feature/(?P<id>[0-9]+)', show_feature, name="show_feature")
]
