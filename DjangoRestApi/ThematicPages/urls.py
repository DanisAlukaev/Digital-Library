from django.conf.urls import url
from ThematicPages import views

"""
Defined routes.

ThematicPages.
/api/ThematicPages: GET, POST, DELETE
/api/ThematicPages/:id GET, PUT, DELETE
"""

urlpatterns = [
    url('(?P<pk>[0-9]+)$', views.thematic_page_detail),
    url('', views.thematic_page_list),
    ]
