import json

from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView

from rest_framework import permissions
from .serializers import *
from .permissions import *


User = get_user_model()


class APIRoot(APIView):
    def get(self, request):

        data = {
            "users": "http://localhost:8000/users/",
            "profiles": "http://localhost:8000/profiles/",
            "posts": "http://localhost:8000/posts/",
            "comments": "http://localhost:8000/comments/",
        }

        return Response(data)


class UserList(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    name = "user-list"
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,
                          IsUserOrReadOnly,)


class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Profile.objects.all()
    serializer_class = UserSerializer
    name = "user-detail"
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,
                          IsUserOrReadOnly,)


class ProfileList(generics.ListCreateAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    name = "profile-list"
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,
                          IsProfileOrReadOnly,)


class ProfileDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileDetailSerializer
    name = "profile-detail"
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,
                          IsProfileOrReadOnly,)


class PostList(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    name = "post-list"
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,
                          PostIsOwnerOrReadOnly,)

    def perform_create(self, serializer):
        serializer.save(profile=self.request.user.profile)


class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostDetailSerializer
    name = "post-detail"
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,
                          PostIsOwnerOrReadOnly,)


class CommentList(generics.ListCreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    name = "comment-list"
    permission_classes = (CommentIsOwnerOrReadOnly,)


class CommentDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    name = "comment-detail"
    permission_classes = (CommentIsOwnerOrReadOnly,)


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

    # Profile as json
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
        first_name, last_name = user['name'].split(" ")
        password = first_name.lower()+"@1234"
        new_user = User.objects.create_user(first_name=first_name,
                                            last_name=last_name,
                                            username=user['username'],
                                            email=user['email'],
                                            password=password)
        Profile.objects.create(id=user['id'],
                               user=new_user,
                               address=address)

    for post in as_json['posts']:
        profile = Profile.objects.get(id=post['user_id'])
        Post.objects.create(id=post['id'],
                            title=post['title'],
                            body=post['body'],
                            profile=profile)

    for comment in as_json['comments']:
        post = Post.objects.get(id=comment['post_id'])
        Comment.objects.create(id=comment['id'],
                               name=comment['name'],
                               email=comment['email'],
                               body=comment['body'],
                               post=post)
