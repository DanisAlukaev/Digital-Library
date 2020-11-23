from django.contrib import admin
from .models import Upload, Tag, Comment, BookmarkPage

# Register Upload, Tag, BookmarkPage models in admin panel
admin.site.register(Upload)
admin.site.register(Tag)
admin.site.register(Comment)
admin.site.register(BookmarkPage)
