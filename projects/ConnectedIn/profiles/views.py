from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from .models import *

def index(request):
    current_profile = current_user(request)
    profiles = None
    return render(request, 'index.html', {"current_user": current_profile, "profiles": profiles})


@login_required
def profile(request, pk):
    current_profile = current_user(request)
    pfl = Profile.objects.get(pk=pk)
    return render(request, 'profile.html', {
        "current_user": current_profile,
        "is_friend": current_profile.is_friend_of(pfl),
        "profile": pfl,
    })


@login_required
def current_user(request):
    return request.user.profile


@login_required
def view_invites(request):
    current_profile = current_user(request)
    return render(request, 'invite.html', {
        "current_user": current_profile,
        "invites": current_profile.invites_made.all(),
        "invited": current_profile.invites_received.all()})


@login_required
def invite(request, pk):
    invited_profile = Profile.objects.get(id=pk)
    current_profile = current_user(request)
    current_profile.invite(invited_profile)
    return render(request, 'invite.html', {
        "current_user": current_profile,
        "invites": current_profile.invites_made.all(),
        "invited": current_profile.invites_received.all()
    })


@login_required
def invite_accept(request, invite_pk):
    accepted_invite = Invite.objects.get(id=invite_pk)
    accepted_invite.accept()
    return redirect('invites')


@login_required
def view_friends(request):
    current_profile = current_user(request)
    return render(request, 'friends.html', {
        "current_user": current_profile,
        "friends": current_profile.friends.all()
    })
