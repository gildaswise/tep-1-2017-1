from django.conf.urls import url
from .views import *

urlpatterns = [
    url(r'^profile/post/$', ViewNewPost.as_view(), name="new_post"),
    url(r'^profile/post/(?P<id>\d+)/$', view_post, name="view_post"),
]
