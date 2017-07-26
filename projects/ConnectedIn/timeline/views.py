from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic.base import View
from django.utils import timezone

from core.views import get_current_profile
from timeline.forms import FormPost
from timeline.models import Post


class ViewNewPost(View):

    def get(self, request, *args, **kwargs):
        pass

    def post(self, request, *args, **kwargs):
        form = FormPost(request.POST, request.FILES)
        data = form.data
        print(data)
        image = form.clean_image()
        if form.is_valid():
            profile = request.user.profile
            post = Post.objects.create(
                profile=profile,
                content=data['content'],
            )
            if image is not None:
                post.image = image
                post.save()
            return redirect('index')
        else:
            return render(request, 'index.html', {'form': form})


def view_post(request, id):
    post = get_object_or_404(Post, id=id)
    return render(request, 'post.html', {'current_profile': get_current_profile(request), 'post': post})


def edit_post(request, id):
    post = get_object_or_404(Post, id=id)
    new_content = request.GET.get('new_content', None)
    new_image = request.GET.get('new_image', None)
    is_edited = post.edit(new_content, new_image)
    data = {'is_edited': is_edited}
    return JsonResponse(data)
