from django.urls import path
from . import views


urlpatterns = [
    path('youtube_clone', views.VideoList.as_view()),
    path('youtube_clone/<int:pk>', views.VideoDetail.as_view())
]