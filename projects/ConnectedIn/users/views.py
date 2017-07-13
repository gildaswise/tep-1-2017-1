from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.views.generic.base import View

from profiles.models import Profile
from users.forms import FormRegisterUser

class ViewRegisterUser(View):

    template = 'register.html'

    def get(self, request):
        return render(request, self.template)

    def post(self, request):
        form = FormRegisterUser(request.POST)
        if form.is_valid():
            data = form.data
            user = User.objects.create(
                username=data['name'].replace(" ", "_").lower(),
                email=data['email'],
                password=data['password'])
            profile = Profile.objects.create(
                name=data['name'],
                phone=data['phone'],
                business=data['business'],
                user=user
            )
            profile.save()
            return redirect('index')
        return render(request, self.template, {'form': form})

