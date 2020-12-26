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

COMMENTS:
/comments/
/comments/:id/: GET, PUT, DELETE
/uploads/comments/:id/: GET
"""

urlpatterns = [
    # For uploads.
    url('uploads/$', views.upload_list),
    url('uploads/(?P<pk>[0-9]+)/$', views.upload_detail),
    url('uploads/status/$', views.upload_status),
    url('uploads/pending/$', views.upload_pending),
    url('uploads/last/(?P<pk>[0-9]+)/$', views.user_contributions),
    # For tags.
    url('tags/', views.tag_list),
    # For comments.
    url('comments/$', views.comment_list),
    url('uploads/comments/(?P<pk>[0-9]+)/$', views.upload_comments),
    url('comments/(?P<pk>[0-9]+)/$', views.comment_detail),
]
