from django.conf.urls import url
from storage import views

"""
Defined routes.

CONTENT:
/api/uploads: GET, POST, DELETE
/api/uploads/:id: GET, PUT, DELETE
/api/uploads/status: GET

TAGS:
/api/tags/: GET
"""

urlpatterns = [
    url('uploads/$', views.upload_list),
    url('uploads/(?P<pk>[0-9]+)/$', views.upload_detail),
    url('uploads/status/$', views.upload_status),
    url('tags/', views.tag_list)
]