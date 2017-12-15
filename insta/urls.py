from . import views
from django.urls import path

app_name = 'insta'
urlpatterns = [
    path('', views.baseView.as_view(), name='base'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=setting.MEDIA_ROOT)