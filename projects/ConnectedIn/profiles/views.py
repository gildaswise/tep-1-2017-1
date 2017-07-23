from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from .models import *


def get_current_profile(request):
    try:
        profile = request.user.profile
        return profile if (isinstance(profile, Profile)) else None
    except:
        return None


def index(request):
    current_profile = get_current_profile(request)
    profiles = None
    if current_profile:
        profiles = Profile.objects.all()
    return render(request, 'index.html', {"current_profile": current_profile, "profiles": profiles})


@login_required
def show_profile(request, pk):
    current_profile = get_current_profile(request)
    pfl = Profile.objects.get(pk=pk)
    return render(request, 'profile.html', {
        "current_profile": current_profile,
        "is_friend": current_profile.is_friend_of(pfl),
        "has_invited": current_profile.has_invited(pfl),
        "profile": pfl,
    })


@login_required
def view_invites(request):
    current_profile = get_current_profile(request)
    return render(request, 'invite.html', {
        "current_profile": current_profile,
        "invites": current_profile.invites_made.all(),
        "invited": current_profile.invites_received.all()})


@login_required
def invite(request, pk):
    invited_profile = Profile.objects.get(id=pk)
    current_profile = get_current_profile(request)
    current_profile.invite(invited_profile)
    return render(request, 'invite.html', {
        "current_profile": current_profile,
        "invites": current_profile.invites_made.all(),
        "invited": current_profile.invites_received.all()
    })


@login_required
def invite_accept(request, invite_pk):
    accepted_invite = Invite.objects.get(id=invite_pk)
    accepted_invite.accept()
    return redirect('invites')


@login_required
def invite_decline(request, invite_pk):
    invite = Invite.objects.get(id=invite_pk)
    invite.delete()
    return redirect('invites')


@login_required
def view_friends(request):
    current_profile = get_current_profile(request)
    return render(request, 'friends.html', {
        "current_profile": current_profile,
        "friends": current_profile.friends.all()
    })
