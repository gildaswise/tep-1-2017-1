from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name="index"),
    url(r'^question/(?P<pk>\d+)$', views.question, name="view_question"),
    url(r'^question/(?P<pk>\d+)/remove$', views.remove, name="remove_question"),
    url(r'^question/(?P<pk>\d+)/results$', views.results, name="results"),
    url(r'^question/(?P<pk>\d+)/manage$', views.manage, name="manage"),
    url(r'^question/(?P<pk>\d+)/toggle', views.toggle, name="toggle_question"),
    url(r'^question/(?P<pk>\d+)/add/(?P<choice_id>\d+)$', views.add_choice, name="add_choice"),
    url(r'^choice/vote/(?P<choice_id>\d+)$', views.vote, name="vote_choice"),
]