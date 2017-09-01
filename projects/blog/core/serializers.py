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

    class Meta:
        model = Comment
        fields = ("url", "name", "email", "body", "post",)


class PostSerializer(serializers.HyperlinkedModelSerializer):

    profile = serializers.SlugRelatedField(queryset=Profile.objects.all(),
                                        slug_field="username")

    class Meta:
        model = Post
        fields = ("url", "title", "body", "profile",)


class PostDetailSerializer(serializers.HyperlinkedModelSerializer):

    profile = serializers.SlugRelatedField(queryset=Profile.objects.all(),
                                        slug_field="username")
    comments = CommentSerializer(many=True, read_only=True)

    class Meta:
        model = Post
        fields = ("url", "title", "body", "profile", "comments",)


class UserSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Profile
        fields = ("url", "id", "username", "email")


class UserDetailSerializer(serializers.HyperlinkedModelSerializer):

    profile = serializers.SlugRelatedField(queryset=Profile.objects.all(),
                                           slug_field="username")

    class Meta:
        model = Profile
        fields = ("url", "id", "username", "email", "first_name", "last_name", "profile")


class ProfileSerializer(serializers.ModelSerializer):

    class Meta:
        model = Profile
        fields = ("url", "id", "username", "email", "name", "address",)


class ProfileDetailSerializer(serializers.ModelSerializer):

    posts = PostSerializer(many=True, read_only=True)

    class Meta:
        model = Profile
        fields = ("url", "id", "username", "email", "name", "address", "posts")


