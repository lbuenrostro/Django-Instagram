from . import views
from django.urls import path

app_name = 'insta'
urlpatterns = [
    path('add/', views.model_form_upload, name="base"),
]