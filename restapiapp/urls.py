from django.urls import path
from .views import movie_api, movie_detail

urlpatterns = [
    path('movie_api/', movie_api),
    path('movie_detail/<slug:slug>/', movie_detail),
]
