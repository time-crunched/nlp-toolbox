from django.conf.urls import url
from django.urls import path

from . import views

app_name = 'sum_v1'
urlpatterns = [
    url(r'^clear/$', views.clear_database, name='clear_database'),
    url(r'^upload/$', views.Upload.as_view(), name='upload'),
    path('summarize', views.Summarize, name='summarize'),
    path('sum_words', views.sum_words, name='sum_words'),
]