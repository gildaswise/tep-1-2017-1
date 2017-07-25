from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^profile/post/$', views.ViewNewPost.as_view(), name="new_post"),
]
