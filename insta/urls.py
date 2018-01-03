from . import views
from django.urls import path

app_name = 'insta'
urlpatterns = [
    path('add/', views.model_form_upload, name="base"),
    path('feed/', views.show_feed, name="feed"),
    path('filter/glass/<image_id>', views.glass_filter, name='glass'),
    path('filter/grey/<image_id>', views.grey_filter, name='grey'),
    path('filter/rain/<image_id>', views.rain_filter, name='rain'),
    path('filter/fire/<image_id>', views.fire_filter, name='fire'),
    path('delete/<image_id>', views.remove, name='delete'),
    path('filter/<image_id>', views.Apply_Filter.as_view(), name='filter'),
]