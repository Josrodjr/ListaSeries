from django.urls import path
from . import views

urlpatterns = [
    path('api/series/', views.SerieListCreate.as_view() ),
]