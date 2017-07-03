from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import *

# Create your views here.

def index(request):
    current_profile = current_user(request)
    return render(request, 'index.html', {"current_user": current_profile, "profiles": Profile.objects.exclude(pk=current_profile.pk)})

def profile(request, pk):
    current_profile = current_user(request)
    pfl = Profile.objects.get(pk=pk)
    return render(request, 'profile.html',{
        "current_user": current_profile,
        "is_friend": current_profile.is_friend_of(pfl),
        "profile": pfl,
    })

def current_user(request):
    return Profile.objects.get(id=3)

def view_invites(request):
    current_profile = current_user(request)
    return render(request, 'invite.html', {
        "current_user": current_profile,
        "invites": current_profile.invites_made.all(),
        "invited": current_profile.invites_received.all()})

def invite(request, pk):
    invited_profile = Profile.objects.get(id=pk)
    current_profile = current_user(request)
    current_profile.invite(invited_profile)
    return render(request, 'invite.html', {
        "current_user": current_profile,
        "invites": current_profile.invites_made.all(),
        "invited": current_profile.invites_received.all()
    })

def invite_accept(request, invite_pk):
    accepted_invite = Invite.objects.get(id=invite_pk)
    accepted_invite.accept()
    return redirect('invites')

def view_friends(request):
    current_profile = current_user(request)
    return render(request, 'friends.html', {
        "current_user": current_profile,
        "friends": current_profile.friends.all()
    })
