from django.contrib import admin
from .models import Upload, Tag


# Register Upload, Tag, ThematicPage model in admin panel
admin.site.register(Upload)
admin.site.register(Tag)

