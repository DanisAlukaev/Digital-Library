from django.conf.urls import url
from user_view import views

"""
Defined routes.

Get Thematic Pages
/api/user_view/thematic_pages_list GET

Get Thematic Pages not available for user
/api/user_view/not_available_pages_list GET

Get Uploads
/api/user_view/thematic_page_uploads/:pk GET

Request an access to thematic page
/api/user_view/request_read_rights/:pk PUT
"""

urlpatterns = [
    url('thematic_pages_list', views.thematic_pages_list),
    url('not_available_pages_list', views.not_available_pages_list),
    url('thematic_page_uploads/(?P<pk>[0-9]+)$', views.thematic_page_uploads),
    url('request_read_rights/(?P<pk>[0-9]+)', views.request_read_rights),
    ]
