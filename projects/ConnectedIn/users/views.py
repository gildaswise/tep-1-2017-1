from django.shortcuts import render, redirect
from django.views.generic.base import View

class ViewRegisterUser(View):

    template = 'register.html'

    def get(self, request):
        return render(request, self.template)

    def post(self, request):
        return render(request, self.template)

