import json
from django.urls import reverse
from django.utils import timezone
from rest_framework import status, generics, viewsets
from rest_framework.decorators import api_view
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from django.shortcuts import render
from rest_framework.views import APIView

from .serializers import *
from .models import *

class APIRoot(APIView):
    def get(self, request):

        data = {
            "users": "http://localhost:8000/users/",
            "groups": "http://localhost:8000/posts/",
            "schedules": "http://localhost:8000/comments/",
        }

        return Response(data)


class UserList(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    name = "user-list"


class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserDetailSerializer
    name = "user-detail"


class PostList(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    name = "post-list"


class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostDetailSerializer
    name = "post-detail"


class CommentList(generics.ListCreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    name = "comment-list"


class CommentDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    name = "comment-detail"


def import_data():
    dump_data = open('db.json', 'r')
    as_json = json.load(dump_data)

    # Post as json
    # {
    #   "user_id": 1,
    #   "id": 1,
    #   "title": "",
    #   "body": "",
    # },

    # Comment as json
    # {
    #     "post_id": 1,
    #     "id": 1,
    #     "name": "",
    #     "email": "",
    #     "body": "",
    # },

    # User as json
    # {
    #     "id": 1,
    #     "name": "Leanne Graham",
    #     "username": "Bret",
    #     "email": "Sincere@april.biz",
    #     "address": {
    #         "street": "Kulas Light",
    #         "suite": "Apt. 556",
    #         "city": "Gwenborough",
    #         "zipcode": "92998-3874",
    #         "geo": {
    #             "lat": "-37.3159",
    #             "lng": "81.1496"
    #         }
    #     }
    # }

    for user in as_json['users']:
        geo = Geo.objects.create(lat=user['address']['geo']['lat'],
                                 lng=user['address']['geo']['lng'])
        address = Address.objects.create(street=user['address']['street'],
                                         suite=user['address']['suite'],
                                         city=user['address']['city'],
                                         zipcode=user['address']['zipcode'],
                                         geo=geo)
        User.objects.create(id=user['id'],
                            name=user['name'],
                            username=user['username'],
                            email=user['email'],
                            address=address)

    for post in as_json['posts']:
        user = User.objects.get(id=post['user_id'])
        Post.objects.create(id=post['id'],
                            title=post['title'],
                            body=post['body'],
                            user=user)

    for comment in as_json['comments']:
        post = Post.objects.get(id=comment['post_id'])
        Comment.objects.create(id=comment['id'],
                               name=comment['name'],
                               email=comment['email'],
                               body=comment['body'],
                               post=post)