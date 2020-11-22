from django.conf.urls import url
from moderators_view import views

"""
Defined routes.

/api/moderate/thematic_pages_list: GET
/api/moderate/thematic_page/:id: GET
/api/moderate/upload/:pk/approve: GET
/api/moderate/upload/:pk/reject: GET
/api/moderate/thematic_page/:pk/user_with_no_access_list: GET
/api/moderate/thematic_page/:pk/user_with_access_list: GET
/api/moderate/thematic_page/:pk/requests: GET
/api/moderate/add_user/:page_pk/:user_pk: POST
"""

urlpatterns = [
    url('thematic_pages_list', views.moderate_pages_list),
    url('thematic_page/(?P<pk>[0-9]+)$', views.moderate_page),
    url('upload/(?P<pk>[0-9]+)/approve', views.approve_upload),
    url('upload/(?P<pk>[0-9]+)/reject', views.reject_upload),
    url('thematic_page/(?P<pk>[0-9]+)/user_with_no_access_list', views.user_with_no_access_list),
    url('thematic_page/(?P<pk>[0-9]+)/user_with_access_list', views.user_with_access_list),
    url('add_user/(?P<page_pk>[0-9]+)/(?P<user_pk>[0-9]+)', views.add_user),
    url('decline_user/(?P<page_pk>[0-9]+)/(?P<user_pk>[0-9]+)', views.decline_user),
    url('thematic_page/(?P<pk>[0-9]+)/requests', views.users_requesting_access),
]
