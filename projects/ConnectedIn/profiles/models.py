from django.db import models

# Create your models here.

class Profile(models.Model):
    name = models.CharField(max_length=64, null=False)
    phone = models.CharField(max_length=12, null=False)
    business = models.CharField(max_length=64, null=False)
    email = models.EmailField(null=False)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def invite(self, invited_profile):
        new_invite = Invite(inviter=self, invited=invited_profile)
        new_invite.save()

    def invite_count(self):
        return self.invites_received.count()

class Invite(models.Model):
    inviter = models.ForeignKey(Profile, related_name="invites_made")
    invited = models.ForeignKey(Profile, related_name="invites_received")
