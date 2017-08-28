from django.shortcuts import render
from .models import *
import json

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