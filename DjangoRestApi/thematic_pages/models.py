from django.db import models
from django.utils import timezone
from django.urls import reverse
from accounts.models import User


class ThematicPage(models.Model):
    title = models.CharField(max_length=200)
    moderators = models.ManyToManyField(User, related_name='can_moderate')
    users = models.ManyToManyField(User, related_name='can_view')
    requested_by = models.ManyToManyField(User, related_name='requested_pages')
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.title
