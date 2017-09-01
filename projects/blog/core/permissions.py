from rest_framework.permissions import *


class IsUserOrReadOnly(BasePermission):

    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return True
        else:
            return obj == request.user


class IsProfileOrReadOnly(BasePermission):

    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return True
        else:
            return obj.user == request.user


class PostIsOwnerOrReadOnly(BasePermission):

    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return True
        else:
            return obj.profile.user == request.user


class CommentIsOwnerOrReadOnly(BasePermission):

    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return True
        else:
            return obj.post.profile.user == request.user
