from django.contrib.auth.models import User
from django.views.generic.base import View
from django.contrib import messages
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm
from django.shortcuts import render, redirect


from profiles.models import Profile
from users.forms import FormRegisterUser


class ViewRegisterUser(View):

    template = 'register.html'

    def get(self, request):
        form = FormRegisterUser()
        return render(request, self.template, {'form': form})

    def post(self, request):
        form = FormRegisterUser(request.POST)
        if form.is_valid():
            data = form.data
            user = User.objects.create_user(
                username=data['name'].replace(" ", "_").lower(),
                email=data['email'],
                password=data['password'])
            profile = Profile.objects.create(
                name=data['name'],
                phone=data['phone'],
                business=data['business'],
                security_question=data['security_question'],
                security_answer=data['security_answer'],
                user=user)
            profile.save()
            return redirect('login')
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
