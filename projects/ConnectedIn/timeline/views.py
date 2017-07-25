from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.views import View
from django.utils import timezone

from timeline.forms import FormPost
from timeline.models import Post


@login_required
class ViewNewPost(View):

    template = 'post.html'

    def get(self, request, *args, **kwargs):
        form = FormPost()
        return render(request, self.template, {'form': form})

    def post(self, request, *args, **kwargs):
        form = FormPost(request.POST, request.FILES)
        data = form.cleaned_data
        image = form.clean_image()
        if form.is_valid():
            profile = request.user.profile
            post = Post.objects.create(
                profile=profile,
                content=data['content']
            )
            if image is not None:
                post.image = image
                post.save()
            return redirect('index')
        else:
            return render(request, self.template, {'form': form})
