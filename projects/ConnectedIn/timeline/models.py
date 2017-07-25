from django.db import models
from django.db.models import CASCADE
from django.utils import timezone
from core.models import Profile


class Post(models.Model):

    profile = models.ForeignKey(Profile, on_delete=CASCADE, related_name='posts')
    content = models.CharField(max_length=256, blank=True, null=False)
    image = models.ImageField(upload_to='images/posts', null=True)
    created_at = models.DateTimeField(null=False)
    edited_at = models.DateTimeField(null=True)
    is_visible = models.BooleanField(default=True, null=False)

    def edit(self, new_content, new_image):
        self.content = new_content
        self.image = new_image
        self.edited_at = timezone.now()
        self.save()

    def delete(self, using=None, keep_parents=False):
        self.is_visible = False
        self.save()
