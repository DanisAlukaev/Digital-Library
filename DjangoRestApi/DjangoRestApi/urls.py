from django.contrib import admin
from django.urls import path
from django.conf.urls import url, include
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/', include('accounts.urls')),
    # Include URL patterns of the storage app.
    url('api/storage/', include('storage.urls')),
    # Include URL patterns of the moderators_view app.
    url('api/moderate/', include('moderators_view.urls')),
    # Include URL patterns of the users_view app.
    url('api/user_view/', include('users_view.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
