from django.db import models

# Create your models here.

class Profile(models.Model):
    name = models.CharField(max_length=64, null=False)
    phone = models.CharField(max_length=12, null=False)
    business = models.CharField(max_length=64, null=False)
    email = models.EmailField(null=False)
    friends = models.ManyToManyField('self', blank=True)

    def __str__(self):
        return "%s" % self.name

    def invite(self, invited_profile):
        new_invite = Invite(inviter=self, invited=invited_profile)
        new_invite.save()

    def is_friend_of(self, profile):
        return self.friends.filter(pk=profile.pk).first() is not None

class Invite(models.Model):
    inviter = models.ForeignKey(Profile, related_name="invites_made")
    invited = models.ForeignKey(Profile, related_name="invites_received")

    def __str__(self):
        return "%s invited %s" % (self.inviter.name, self.invited.name)

    def accept(self):
        self.inviter.friends.add(self.invited)
        self.invited.friends.add(self.inviter)
        self.delete()
