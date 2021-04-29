from django.urls import path
from . import views


urlpatterns = [
    path('youtube_clone/comments', views.CommentList.as_view()),
    path('youtube_clone/comments/<int:pk>', views.CommentDetail.as_view())
]