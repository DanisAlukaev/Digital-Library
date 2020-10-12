from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='Storage-workspace'),
    path('about/', views.about, name='Storage-about'),
]
