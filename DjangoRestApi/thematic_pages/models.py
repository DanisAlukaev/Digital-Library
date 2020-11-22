from django.db import models
from accounts.models import User


class ThematicPage(models.Model):
    """
    Class used to model thematic pages.
    Describes attributes of a thematic page, e.g. title, moderators, users, requested_by, description.
    """

    # Implement attributes of ThematicPage entity according to ER schema.
    # Title of a thematic page.
    title = models.CharField(max_length=200)
    # Moderators of a page.
    moderators = models.ManyToManyField(User, default=None, null=True, blank=True, related_name='can_moderate')
    # Followers of a page.
    users = models.ManyToManyField(User, default=None, null=True, blank=True, related_name='can_view')
    # Users who requested joining to a page.
    requested_by = models.ManyToManyField(User, default=None, null=True, blank=True, related_name='requested_pages')
    # Description of a page.
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.title
