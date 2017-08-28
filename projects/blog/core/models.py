from django.db import models


class Geo(models.Model):
    lat = models.FloatField()
    lng = models.FloatField()


class Address(models.Model):
    street = models.CharField(max_length=128)
    suite = models.CharField(max_length=128)
    city = models.CharField(max_length=128)
    zipcode = models.CharField(max_length=10)
    geo = models.ForeignKey(Geo)


class User(models.Model):
    username = models.CharField(max_length=128)
    name = models.CharField(max_length=128)
    email = models.EmailField()
    address = models.ForeignKey(Address)


class Post(models.Model):
    title = models.CharField(max_length=128)
    body = models.TextField()
    user = models.ForeignKey(User, related_name="posts")


class Comment(models.Model):
    name = models.CharField(max_length=128)
    email = models.EmailField()
    body = models.TextField()
    post = models.ForeignKey(Post, related_name="comments")