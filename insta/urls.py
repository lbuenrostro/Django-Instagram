from . import views
from django.urls import path

app_name = 'insta'
urlpatterns = [
    path('add/', views.model_form_upload, name="base"),
    path('feed/', views.show_feed, name="feed"),
    path('filter/glass/<image_id>', views.glass_filter, name='glass'),
    path('filter/grey/<image_id>', views.grey_filter, name='grey')
]