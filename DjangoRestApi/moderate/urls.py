from django.conf.urls import url
from moderate import views

"""
Defined routes.

Get Thematic Pages
/api/moderate/thematic_pages_list GET

Moderate Thematic Page
/api/moderate/thematic_page/:id GET

Moderate Upload
/api/moderate/upload/:id/approve PUT
/api/moderate/upload/:id/reject PUT

Get Users with access and without access to Thematic Page
/api/moderate/thematic_page/:id/user_with_no_access_list GET
/api/moderate/thematic_page/:id/user_with_access_list GET
"""

urlpatterns = [
    url('thematic_pages_list', views.moderate_pages_list),
    url('thematic_page/(?P<pk>[0-9]+)$', views.moderate_page),
    url('upload/(?P<pk>[0-9]+)/approve', views.approve_upload),
    url('upload/(?P<pk>[0-9]+)/reject', views.reject_upload),
    url('thematic_page/(?P<pk>[0-9]+)/user_with_no_access_list', views.user_with_no_access_list),
    url('thematic_page/(?P<pk>[0-9]+)/user_with_access_list', views.user_with_access_list),
    url('add_user/(?P<page_pk>[0-9]+)/(?P<user_pk>[0-9]+)', views.add_user),
    ]
