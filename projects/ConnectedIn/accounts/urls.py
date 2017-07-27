from django.conf.urls import url
from django.contrib.auth import views
from .views import *

urlpatterns = [
    url(r'^register/$', ViewRegisterUser.as_view(), name="register"),
    url(r'^forgot/$', ViewForgotPasswordVerification.as_view(), name="forgot_password"),
    url(r'^forgot/(?P<token>.+)$', ViewForgotPasswordNew.as_view(), name="new_password"),
    url(r'^register/$', ViewRegisterUser.as_view(), name="register"),
    url(r'^edit/$', ViewEditUser.as_view(), name="edit"),
    url(r'^login/$', views.LoginView.as_view(template_name="login.html"), name='login'),
    url(r'^logout/$', views.LogoutView.as_view(template_name="login.html"), name='logout'),
    url(r'^password/$', change_password, name='change_password'),
]