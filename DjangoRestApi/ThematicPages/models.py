from django.db import models
from django.utils import timezone
from django.urls import reverse
from accounts.models import User


class ThematicPage(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name
