from django.conf.urls import url, include
from rest_framework import routers
from rest_framework.routers import DefaultRouter

from .views import *

urlpatterns = [
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^$', APIRoot.as_view(), name='root'),
    url(r'^users/$',
        UserList.as_view(),
        name=UserList.name),
    url(r'^users/(?P<pk>[0-9]+)/$',
        UserDetail.as_view(),
        name=UserDetail.name),
    url(r'^profiles/$',
        ProfileList.as_view(),
        name=ProfileList.name),
    url(r'^profiles/(?P<pk>[0-9]+)/$',
        ProfileDetail.as_view(),
        name=ProfileDetail.name),
    url(r'^posts/$',
        PostList.as_view(),
        name=PostList.name),
    url(r'^posts/(?P<pk>[0-9]+)/$',
        PostDetail.as_view(),
        name=PostDetail.name),
    url(r'^comments/$',
        CommentList.as_view(),
        name=CommentList.name),
    url(r'^comments/(?P<pk>[0-9]+)/$',
        CommentDetail.as_view(),
        name=CommentDetail.name),
]
