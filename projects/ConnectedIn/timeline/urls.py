from django.conf.urls import url
from .views import *

urlpatterns = [
    url(r'^post/$', ViewNewPost.as_view(), name="new_post"),
    url(r'^post/(?P<id>\d+)/$', view_post, name="view_post"),
    url(r'^post/edit/(?P<id>\d+)/$', edit_post, name="edit_post"),
]
