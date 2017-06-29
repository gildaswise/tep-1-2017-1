from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    status = models.CharField(max_length=64)

class Friendship(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name="friends")
    friend = models.ForeignKey(Profile, on_delete=models.CASCADE)
    date_added = models.DateField()

class Chat(models.Model):
    date_created = models.DateField()

class SingleChat(Chat):
    friendship = models.ForeignKey(Friendship)

class GroupChat(Chat):
    title = models.CharField(max_length=64)

class GroupMember(models.Model):
    chat = models.ForeignKey(GroupChat, on_delete=models.CASCADE, related_name="members")
    friendship = models.ForeignKey(Friendship, on_delete=models.CASCADE)

class Message(models.Model):
    chat = models.ForeignKey(Chat, related_name="messages", on_delete=models.CASCADE)
    sent_by = models.ForeignKey(Profile)
    content = models.TextField(blank=True)
    timestamp = models.DateTimeField()
