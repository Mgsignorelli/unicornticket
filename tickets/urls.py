from django.conf.urls import url
from tickets.views import create_ticket, vote_bug, show_bug, show_feature, index_bug, index_feature, vote_feature, \
    add_comment

urlpatterns = [
    url(r'^ticket/create', create_ticket, name="create_ticket"),
    url(r'^bug/(?P<id>[0-9]+)/vote/(?P<direction>(up|down))', vote_bug, name="vote_bug"),
    url(r'^bug/(?P<id>[0-9]+)/comment', add_comment, name="comment_bug"),
    url(r'^bug/(?P<id>[0-9]+)', show_bug, name="show_bug"),
    url(r'^feature/(?P<id>[0-9]+)/vote/up', vote_feature, name="vote_feature"),
    url(r'^feature/(?P<id>[0-9]+)/comment', add_comment, name="comment_feature"),
    url(r'^feature/(?P<id>[0-9]+)', show_feature, name="show_feature"),
    url(r'^bug', index_bug, name="index_bug"),
    url(r'^feature', index_feature, name="index_feature")
]
