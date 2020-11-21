from django.urls import path, include
from accounts import views

"""
Methods     Urls                Action
POST        auth/users/         Creates new user. 
                                Attribute first_name, last_name, email, password, re_password
                                should be specified.
POST        auth/token/login/   Creates new token "token" for a user specified by email and password.
POST        auth/token/logout/  Log-out a user with token "token".
GET         auth/users/me/      Returns information about a user with token "token".
GET         auth/create_token/  Creates token session for a user with passed in parameters id.
"""

urlpatterns = [
    # Djoser initialization.
    path('', include('djoser.urls')),
    path('', include('djoser.urls.authtoken')),
    # Create new token session. Used only after registration.
    path('create_token/', views.create_token)
]
