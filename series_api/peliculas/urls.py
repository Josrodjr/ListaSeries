from django.urls import path
from . import views

urlpatterns = [
    path('api/peliculas/', views.PeliculaListCreate.as_view() ),
]