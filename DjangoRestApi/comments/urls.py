from django.conf.urls import url
from .views import comment_list, comment_detail


urlpatterns = [
    url('comments/$', comment_list),
    url('comments/(?P<pk>[0-9]+)/$', comment_detail),
]
