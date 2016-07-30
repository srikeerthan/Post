from __future__ import unicode_literals

from django.conf import settings
# from django.contrib.auth.models import User
from django.db import models

# Create your models here.
from django.utils.encoding import python_2_unicode_compatible


@python_2_unicode_compatible
class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='post')
    photo = models.ImageField()
    caption = models.CharField(max_length=150, blank=True)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = 'Posts'
        ordering = ['-date_created', ]

    def __str__(self):
        return self.caption

@python_2_unicode_compatible
class Like(models.Model):
    post = models.ForeignKey(Post, related_name='liked_post')
    user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='liker')
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '{}:{}'.format(self.user,self.post)
