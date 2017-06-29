from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import *

# Create your views here.

def index(request):
    return render(request, 'index.html', {"profiles": Profile.objects.all()})

def profile(request, pk):
    pfl = Profile.objects.get(pk=pk)
    return render(request, 'profile.html', {"profile": pfl})

def current_user(request):
    return Profile.objects.get(id=1)

def invite(request, pk):
    invited_profile = Profile.objects.get(id=pk)
    current_profile = current_user(request)
    current_profile.invite(invited_profile)
    return render(request, 'invite.html',
                  {
                      "invites": current_profile.invites_made.all(),
                      "invited": current_profile.invites_received.all()
                  })
