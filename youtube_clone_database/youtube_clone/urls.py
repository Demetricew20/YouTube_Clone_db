from django.urls import path
from . import views


urlpatterns = [
    path('youtube_clone', views.VideoList.as_view())
]