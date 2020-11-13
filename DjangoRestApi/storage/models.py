from django.db import models


class Upload(models.Model):
    """
    Dummy model to show interconnection process.
    Contains three fields: title, description, and published.
    Do not forget to migrate Data Model to the database.
    """
    title = models.CharField(max_length=70, blank=False, default='')
    description = models.CharField(max_length=200, blank=False, default='')
    published = models.BooleanField(default=False)
