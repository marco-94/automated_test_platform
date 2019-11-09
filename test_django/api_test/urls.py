from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^index/$', views.index, name="index"),
    url(r'^user/$', views.user, name="user"),
    url(r'^project/$', views.project, name="project"),
]
