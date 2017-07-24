from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name="index"),
    url(r'^profile/(?P<pk>\d+)/$', views.show_profile, name="show_profile"),
    url(r'^profile/(?P<pk>\d+)/invite$', views.invite_profile, name="invite_profile"),
    url(r'^profile/(?P<invite_pk>\d+)/accept$', views.invite_accept, name="invite_accept"),
    url(r'^profile/(?P<invite_pk>\d+)/decline$', views.invite_decline, name="invite_decline"),
    url(r'^invites$', views.view_invites, name="invites"),
    url(r'^friends$', views.view_friends, name="friends"),
    url(r'^friends/(?P<friend_pk>\d+)/remove$', views.remove_a_friend, name="remove_a_friend"),
]
