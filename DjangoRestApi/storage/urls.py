from django.conf.urls import url
from storage import views

"""
Defined routes.

CONTENT.
/api/uploads: GET, POST, DELETE
/api/uploads/:id: GET, PUT, DELETE
/api/uploads/published: GET

TAGS.
/api/tags/: GET
"""

urlpatterns = [
    url('ThematicPages/$', views.thematic_page_list),
    url('ThematicPages/<slug:page_name>/$', views.thematic_page_detail),
    url('uploads/$', views.upload_list),
    url('uploads/(?P<pk>[0-9]+)/$', views.upload_detail),
    url('uploads/status/$', views.upload_status),
    url('tags/', views.tag_list),
]