from django.contrib.auth.models import User
from django.db import models


class Profile(models.Model):

    DEFAULT_QUESTIONS = (
        (1, "What is your pet's name?"),
        (2, "Where were you born?"),
        (3, "What is your main nickname?"),
    )

    user = models.OneToOneField(User, related_name="profile", on_delete=models.CASCADE)
    name = models.CharField(max_length=64, null=False)
    phone = models.CharField(max_length=12, null=False)
    business = models.CharField(max_length=32, null=False)
    security_question = models.CharField(max_length=1, null=False, choices=DEFAULT_QUESTIONS, default=1)
    security_answer = models.CharField(max_length=64, null=False)
    friends = models.ManyToManyField('self', blank=True)

    def __str__(self):
        return "%s" % self.name

    def delete(self, using=None, keep_parents=False):
        user = self.user
        super(Profile, self).delete(using, keep_parents)
        user.delete()

    @property
    def email(self):
        return self.user.email

    def invite(self, invited_profile):
        new_invite = Invite(inviter=self, invited=invited_profile)
        new_invite.save()

    def is_friend_of(self, profile):
        return self.friends.filter(pk=profile.pk).first() is not None

    def has_invited(self, profile):
        return self.invites_made.filter(invited=profile).first() is not None

    def remove_friend(self, profile):
        if self.is_friend_of(profile):
            self.friends.remove(profile)

    def is_blocked_by(self, profile):
        return self.blocks_received.filter(blocker=profile).first() is not None

    def has_blocked(self, profile):
        return self.blocks_made.filter(blocked=profile).first() is not None

    def block(self, profile):
        Block.objects.create(blocker=self, blocked=profile)
        if self.is_friend_of(profile):
            self.remove_friend(profile)

    def remove_block(self, profile):
        if self.has_blocked(profile):
            self.blocks_made.filter(blocker=self, blocked=profile).first().delete()


class Invite(models.Model):

    invitee = models.ForeignKey(Profile, related_name="invites_made")
    invited = models.ForeignKey(Profile, related_name="invites_received")

    def __str__(self):
        return "%s invited %s" % (self.invitee.name, self.invited.name)

    def accept(self):
        self.invitee.friends.add(self.invited)
        self.invited.friends.add(self.invitee)
        self.delete()


class Block(models.Model):

    blocker = models.ForeignKey(Profile, related_name="blocks_made")
    blocked = models.ForeignKey(Profile, related_name="blocks_received")

    def __str__(self):
        return "%s blocked %s" % (self.blocker.name, self.blocked.name)
