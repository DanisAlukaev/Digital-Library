from django.urls import path
from .views import (
    UploadListView,
    UploadDetailView,
    UploadCreateView,
    UploadUpdateView,
    UploadDeleteView
)
from . import views

urlpatterns = [
    path('', UploadListView.as_view(), name='Storage-workspace'),
    path('content/<int:pk>/', UploadDetailView.as_view(), name='Content-detail'),
    path('content/new/', UploadCreateView.as_view(), name='Content-create'),
    path('content/<int:pk>/update/', UploadUpdateView.as_view(), name='Content-update'),
    path('content/<int:pk>/delete/', UploadDeleteView.as_view(), name='Content-delete'),
    path('about/', views.about, name='Storage-about'),
]
