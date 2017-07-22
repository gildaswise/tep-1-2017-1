from django.conf.urls import url
from django.contrib.auth import views
from .views import *

urlpatterns = [
    url(r'^register/$', ViewRegisterUser.as_view(), name="register"),
    url(r'^login/$', views.LoginView.as_view(template_name="login.html"), name='login'),
    url(r'^logout/$', views.LogoutView.as_view(template_name="login.html"), name='logout'),
    url(r'^password/$', change_password, name='change_password'),
]