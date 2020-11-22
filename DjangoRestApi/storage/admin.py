from django.contrib import admin
from .models import Upload, Tag, Comment

# Register Upload, Tag model in admin panel
admin.site.register(Upload)
admin.site.register(Tag)
admin.site.register(Comment)
