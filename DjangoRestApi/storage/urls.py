from django.conf.urls import url
from storage import views

"""
Defined routes:
/api/uploads: GET, POST, DELETE
/api/uploads/:id: GET, PUT, DELETE
/api/uploads/published: GET
"""

urlpatterns = [
    url('uploads/$', views.upload_list),
    url('uploads/(?P<pk>[0-9]+)/$', views.upload_detail),
    url('uploads/published/$', views.upload_list_published)
]