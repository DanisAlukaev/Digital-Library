from django.conf.urls import url
from user_view import views

"""
Defined routes.

Get Thematic Pages
/api/user_view/thematic_pages_list GET

Get Uploads
/api/user_view/thematic_page:id GET
"""

urlpatterns = [
    url('thematic_pages_list', views.thematic_pages_list),
    url('thematic_page/(?P<pk>[0-9]+)$', views.thematic_page),
    ]
