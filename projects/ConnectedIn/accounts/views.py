from django.contrib.auth.models import User
from django.views.generic.base import View
from django.contrib import messages
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm
from django.shortcuts import render, redirect
from datetime import datetime, timedelta
from django.utils import timezone, timesince

from core.models import Profile, Token
from accounts.forms import *


class ViewRegisterUser(View):

    template = 'register.html'

    def get(self, request, *args, **kwargs):
        form = FormRegisterUser()
        return render(request, self.template, {'form': form})

    def post(self, request, *args, **kwargs):
        form = FormRegisterUser(request.POST, request.FILES)
        if form.is_valid():
            data = form.data
            user = User.objects.create_user(
                username=data['name'].replace(" ", "_").lower(),
                email=data['email'],
                password=data['password'])
            avatar = form.clean_avatar()
            profile = Profile.objects.create(
                name=data['name'],
                phone=data['phone'],
                business=data['business'],
                security_question=data['security_question'],
                security_answer=data['security_answer'],
                avatar=avatar,
                user=user)
            profile.save()
            return redirect('login')
        return render(request, self.template, {'form': form})


class ViewForgotPasswordVerification(View):

    template = 'forgot_password_verif.html'

    def get(self, request, *args, **kwargs):
        form = FormForgotPasswordVerification()
        return render(request, self.template, {'form': form})

    def post(self, request, *args, **kwargs):
        form = FormForgotPasswordVerification(request.POST)
        if form.is_valid():
            date_until = datetime.now() + timedelta(minutes=10)
            token = Token.objects.create(until=date_until)
            return redirect('new_password', token=token.uuid)
        else:
            return render(request, self.template, {'form': form})


class ViewForgotPasswordNew(View):

    template = 'forgot_password_new.html'

    def get(self, request, *args, **kwargs):
        form = FormForgotPasswordNew()
        uuid = kwargs['token']
        token = Token.objects.get(uuid=uuid)
        print("Refused password renewal with token ", token)
        if token.is_valid():
            return render(request, self.template, {'form': form})
        else:
            return redirect('forgot_password')

    def post(self, request, *args, **kwargs):
        form = FormForgotPasswordNew(request.POST)
        if form.is_valid():
            data = form.data
            user = User.objects.get(email=data['email'])
            user.set_password(data['new_password2'])
            user.save()
            update_session_auth_hash(request, user)
            return redirect('login')
        else:
            return render(request, self.template, {'form': form})


# https://simpleisbetterthancomplex.com/tips/2016/08/04/django-tip-9-password-change-form.html
def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            return redirect('index')
        else:
            return render(request, 'change_password.html', {'form': form})
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'change_password.html', {'form': form})
