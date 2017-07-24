from django.contrib.auth.models import User
from django.db import models


class Profile(models.Model):

    user = models.OneToOneField(User, related_name="profile", on_delete=models.CASCADE)
    name = models.CharField(max_length=64, null=False)
    phone = models.CharField(max_length=12, null=False)
    business = models.CharField(max_length=64, null=False)
    friends = models.ManyToManyField('self', blank=True)

    def __str__(self):
        return "%s" % self.name

    @property
    def email(self):
        return self.user.email

    def invite(self, invited_profile):
        new_invite = Invite(inviter=self, invited=invited_profile)
        new_invite.save()

    def is_friend_of(self, profile):
        return self.friends.filter(pk=profile.pk).first() is not None

    def has_invited(self, profile):
        return self.invites_made.filter(invited=profile) is not None

    def remove_friend(self, profile):
        if self.is_friend_of(profile):
            self.friends.filter(pk=profile.pk).first().delete()


class Invite(models.Model):

    invitee = models.ForeignKey(Profile, related_name="invites_made")
    invited = models.ForeignKey(Profile, related_name="invites_received")

    def __str__(self):
        return "%s invited %s" % (self.invitee.name, self.invited.name)

    def accept(self):
        self.invitee.friends.add(self.invited)
        self.invited.friends.add(self.invitee)
        self.delete()
