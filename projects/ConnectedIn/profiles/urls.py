from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name="index"),
    url(r'^profile/(?P<pk>\d+)/$', views.profile, name="show_profile"),
    url(r'^profile/(?P<pk>\d+)/invite$', views.invite, name="invite_profile"),
    url(r'^invites$', views.invites, name="invites"),
]
