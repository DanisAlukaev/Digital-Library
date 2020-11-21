from django.db import models
from django.utils import timezone
from django.urls import reverse
from accounts.models import User
from thematic_pages.models import ThematicPage


class Tag(models.Model):
    """
    Class used to tag uploads.
    Tags are unique and have one field: name.
    """

    # Implement attributes of Tag entity according to ER schema.
    name = models.CharField(max_length=200, unique=True)

    def natural_key(self):
        return self.name

    def __str__(self):
        return self.name


class Upload(models.Model):
    """
    Class used to model uploads. Describes attributes of an upload, e.g. title, user, type, date, status, innopoints,
    tags, link, thematic_page, rating, file.
    """

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
    # Title of an upload.
    title = models.CharField(max_length=100)
    # Uploader.
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    # Type of an upload, either document, image, video, or link.
    type = models.IntegerField(choices=Types.choices, default=0)
    # Date of an upload.
    date = models.DateTimeField(default=timezone.now)
    # Status of an upload, either rejected, approved, or pending.
    status = models.IntegerField(choices=Statuses.choices, default=2)
    # Assigned by a moderator innopoints.
    innopoints = models.IntegerField(default=0)
    # Assigned tags.
    tags = models.ManyToManyField(Tag, null=True, blank=True)
    # In case it has a type of link, in link field user can pass a link to an interested resource.
    link = models.CharField(max_length=150, default=None, null=True, blank=True)
    # Thematic page where upload is placed.
    thematic_page = models.ForeignKey(ThematicPage, default=None, null=True, blank=True, on_delete=models.CASCADE)
    # Rating of a resource.
    rating = models.FloatField(default=0, null=True, blank=True)
    # In case it has not a type of link, in file field user can put an interested file.
    file = models.FileField(upload_to='files/', default='files/None/No-doc.pdf', null=True, blank=True)

    def __str__(self):
        return self.title


class BookmarkPage(models.Model):
    """
    Class used to model bookmark pages. Describes attributes of an upload, e.g. title, user, uploads.
    """

    # Implement attributes of BookmarkPage entity according to ER schema.
    # Title of a bookmark page.
    title = models.CharField(max_length=200)
    # User who owns this bookmark page.
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    # Favorite uploads.
    uploads = models.ManyToManyField(Upload, null=True)

    def __str__(self):
        return self.title
