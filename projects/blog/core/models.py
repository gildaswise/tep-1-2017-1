from django.db import models


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


class User(models.Model):
    username = models.CharField(max_length=128)
    name = models.CharField(max_length=128)
    email = models.EmailField()
    address = models.ForeignKey(Address)

    def __str__(self):
        return "@%s - %s - %s" % (self.username, self.name, self.email)


class Post(models.Model):
    title = models.CharField(max_length=128)
    body = models.TextField()
    user = models.ForeignKey(User, related_name="posts")

    def __str__(self):
        return "Post from @%s - %s" % (self.user.username, self.title)


class Comment(models.Model):
    name = models.CharField(max_length=128)
    email = models.EmailField()
    body = models.TextField()
    post = models.ForeignKey(Post, related_name="comments")

    def __str__(self):
        return "Comment from %s" % (self.name)