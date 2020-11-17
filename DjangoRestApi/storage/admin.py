from django.contrib import admin
from .models import Upload, Tag, ThematicPage


# Register Upload, Tag, ThematicPage model in admin panel
admin.site.register(Upload)
admin.site.register(Tag)
admin.site.register(ThematicPage)
