from django.contrib import admin
from django.urls import path
from django.conf.urls import url, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/', include('accounts.urls')),
    # Include URL patterns from storage app
    url('api/storage/', include('storage.urls')),
    # Include URL patterns from ThematicPages app
    url('api/ThematicPages/', include('ThematicPages.urls')),
]
