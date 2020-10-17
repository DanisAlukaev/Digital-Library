from django.db import models
from django.utils import timezone
from django.urls import reverse
from django.contrib.auth.models import User


class Upload(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField()
    date = models.DateTimeField(default=timezone.now)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('Content-detail', kwargs={'pk': self.pk})
