from django.db import models
from django.utils import timezone
from django.urls import reverse
from accounts.models import User


class ThematicPage(models.Model):
    name = models.CharField(max_length=200, help_text="Enter the name for thematic page")

    def __str__(self):
        return self.name


class Tag(models.Model):
    # Implement attributes of Tag entity according to ER schema.
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Upload(models.Model):

    # Create auxiliary classes to explicitly specify options for types and statuses.
    class Types(models.IntegerChoices):
        DOCUMENT = 0
        IMAGE = 1
        VIDEO = 2
        LINK = 3

    class Statuses(models.IntegerChoices):
        REJECTED = 0
        APPROVED = 1
        PENDING = 2

    # Implement attributes of Upload entity according to ER schema.
    title = models.CharField(max_length=50)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    type = models.IntegerField(choices=Types.choices, default=0)
    date = models.DateTimeField(default=timezone.now)
    status = models.IntegerField(choices=Statuses.choices, default=2)
    innopoints = models.IntegerField(default=0)
    tags = models.ManyToManyField(Tag)
    link = models.CharField(max_length=150, default=None, null=True, blank=True)
    thematic_page = models.ForeignKey(ThematicPage, on_delete=models.CASCADE)

    # thematic_page = models.CharField(max_length=50)
    # file = models.FileField(upload_to='media/')

    def __str__(self):
        return self.title
