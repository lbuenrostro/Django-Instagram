from . import views
from django.urls import path

app_name = 'insta'
urlpatterns = [
    path('feed/', views.model_form_upload, name="base"),
    path('upload/', views.upload_pic, name="index"),
]