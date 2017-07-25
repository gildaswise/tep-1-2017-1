from django.db import models
from django.db.models import CASCADE
from django.utils import timezone


class Post(models.Model):

    profile = models.ForeignKey('core.Profile', on_delete=CASCADE, related_name='posts')
    content = models.CharField(max_length=256, blank=True, null=False)
    image = models.ImageField(upload_to='posts', null=True)
    created_at = models.DateTimeField(null=False)
    edited_at = models.DateTimeField(null=True)
    is_visible = models.BooleanField(default=True, null=False)

    def __str__(self):
        to_str = "%s posted by %s" % (self.content, self.profile)
        if self.image:
            to_str += " with image"
        to_str += " at %s" % self.created_at
        if self.edited_at != self.created_at:
            to_str += " and edit at %s" % self.edited_at
        return to_str

    def edit(self, new_content, new_image):
        self.content = new_content
        self.image = new_image
        self.edited_at = timezone.now()
        self.save()

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):
        if self.created_at is None:
            self.created_at = timezone.now()
        if self.edited_at is None:
            self.edited_at = self.created_at
        super(Post, self).save(force_insert, force_update, using, update_fields)

    def delete(self, using=None, keep_parents=False):
        self.is_visible = False
        self.save()
