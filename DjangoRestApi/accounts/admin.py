from django.contrib import admin
from .models import User

admin.site.register(User)
AUTH_USER_MODEL = 'models.User'