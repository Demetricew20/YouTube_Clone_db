from django.urls import path
from . import views


urlpatterns = [
    path('comments'),
    path('comments/<int:pk>')
]