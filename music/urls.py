from django.contrib import admin
from django.urls import path
from django.conf.urls import url
from . import views

app_name="music"

urlpatterns = [
    #/nusic/
    url(r'^$',views.IndexView.as_view(), name='index'),

    #/music/71
    url(r'^(?P<pk>[0-9]+)/$',views.DetailView.as_view(), name='detail'),

    #/music/<album_id>/favorite/
    url(r'^(?P<album_id>[0-9]+)/favorite/$',views.favorite, name='favorite'),
]
