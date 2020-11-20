from __future__ import unicode_literals
from django.urls import reverse
from django.utils import timezone
from django.contrib.auth.models import User
from Storage.models import Upload
from django.conf import settings
from django.db import models




class Comment(models.Model):
    content_connected = models.ForeignKey(
        Upload, related_name='comments', on_delete=models.CASCADE)

    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)

    class Meta:
        ordering = ['-date_posted']

    def number_of_comments(self):
        return Comment.objects.filter(content_connected=self).count()

    def __str__(self):
        return 'Comment by {} on {}'.forms(self.author.username, self.content_connected.title)
    def get_absolute_url(self):
        return reverse("comments:thread", kwargs={"id": self.id})

    def get_delete_url(self):
       return reverse("comments:delete", kwargs={"id": self.id})

    def __unicode__(self):
        return str(self.user.username)
