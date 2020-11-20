from django.conf.urls import url, include
from thematic_pages import views

"""
Defined routes.
thematic_pages.
/api/thematic_pages: GET, POST, DELETE
/api/thematic_pages/:id GET, PUT, DELETE
"""

urlpatterns = [
    url('(?P<pk>[0-9]+)$', views.thematic_page_detail),
    url('', views.thematic_page_list),
]
