from django.urls import path

from . import views

app_name = 'sim_v1'
urlpatterns = [
	path('calculate', views.calculate, name = 'calculate'),
    path('upload', views.model_form_upload, name = 'upload')
]