from django.urls import path
from .views import (
    UploadListView,
    UploadDetailView,
    UploadCreateView,
    UploadUpdateView,
    UploadDeleteView,
    UserUploadListView,
    UploadWithFilters,
)
from . import views

urlpatterns = [
    path('', UploadListView.as_view(), name='Storage-workspace'),
    path('user/<str:username>/', UserUploadListView.as_view(), name='User-uploads'),
    path('content/<int:pk>/', UploadDetailView.as_view(), name='Content-detail'),
    path('content/new/', UploadCreateView.as_view(), name='Content-create'),
    path('content/<int:pk>/update/', UploadUpdateView.as_view(), name='Content-update'),
    path('content/<int:pk>/delete/', UploadDeleteView.as_view(), name='Content-delete'),
    path('about/', views.about, name='Storage-about'),
    path('search_and_filter/', views.search_and_filter, name='Search_and_filter'),
    path('show_with_filters', UploadWithFilters.as_view(), name="Show_with_filters")
]
