from django.contrib import admin
from .models import *

admin.site.register(Geo)
admin.site.register(Address)
admin.site.register(User)
admin.site.register(Post)
admin.site.register(Comment)