from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class Geo(models.Model):
    lat = models.FloatField()
    lng = models.FloatField()

    def __str__(self):
        return "lat: %s\nlng:%s" % (self.lat, self.lng)


class Address(models.Model):
    street = models.CharField(max_length=128)
    suite = models.CharField(max_length=128)
    city = models.CharField(max_length=128)
    zipcode = models.CharField(max_length=10)
    geo = models.ForeignKey(Geo)

    def __str__(self):
        return "%s, %s, %s, %s at %s" % (self.street, self.suite, self.city, self.zipcode, self.geo)


class Profile(models.Model):
    user = models.ForeignKey(User, related_name="profile", on_delete=models.CASCADE)
    address = models.ForeignKey(Address)

    @property
    def username(self):
        return self.user.username

    @property
    def name(self):
        return self.user.first_name + " " + self.user.last_name

    @property
    def email(self):
        return self.user.email

    def __str__(self):
        return "@%s - %s - %s" % (self.username, self.name, self.email)


class Post(models.Model):
    title = models.CharField(max_length=128)
    body = models.TextField()
    profile = models.ForeignKey(Profile, related_name="posts", on_delete=models.CASCADE)

    def __str__(self):
        return "Post from @%s - %s" % (self.profile.username, self.title)


class Comment(models.Model):
    name = models.CharField(max_length=128)
    email = models.EmailField()
    body = models.TextField()
    post = models.ForeignKey(Post, related_name="comments", on_delete=models.CASCADE)

    def __str__(self):
        return "Comment from %s" % (self.name)