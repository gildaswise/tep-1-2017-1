from rest_framework import serializers
from .models import *


class GeoSerializer(serializers.ModelSerializer):

    class Meta:
        model = Geo
        fields = ("url", "id", "lat", "lng",)


class AddressSerializer(serializers.ModelSerializer):

    class Meta:
        model = Address
        fields = ("url", "id", "street", "suite", "city", "zipcode",)


class CommentSerializer(serializers.HyperlinkedModelSerializer):

    post = serializers.SlugRelatedField(queryset=Post.objects.all(),
                                          slug_field="title")

    class Meta:
        model = Comment
        fields = ("url", "name", "email", "body", "post",)


class PostSerializer(serializers.HyperlinkedModelSerializer):

    user = serializers.SlugRelatedField(queryset=User.objects.all(),
                                        slug_field="username")

    class Meta:
        model = Post
        fields = ("url", "title", "body", "user",)


class PostDetailSerializer(serializers.HyperlinkedModelSerializer):

    user = serializers.SlugRelatedField(queryset=User.objects.all(),
                                        slug_field="username")
    comments = CommentSerializer(many=True, read_only=True)

    class Meta:
        model = Post
        fields = ("url", "title", "body", "user", "comments",)


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ("url", "id", "username", "email", "name", "address",)

class UserDetailSerializer(serializers.ModelSerializer):

    posts = PostSerializer(many=True, read_only=True)

    class Meta:
        model = User
        fields = ("url", "id", "username", "email", "name", "address", "posts")


