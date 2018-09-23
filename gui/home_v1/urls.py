from django.urls import path

from . import views

app_name = 'home_v1'
urlpatterns = [
    path('index', views.index, name = 'index')
]