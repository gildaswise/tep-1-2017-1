from django.contrib import admin
from .models import *

admin.site.register(Geo)
admin.site.register(Address)
admin.site.register(Profile)
admin.site.register(Post)
admin.site.register(Comment)