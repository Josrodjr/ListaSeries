from django.urls import path
from . import views

urlpatterns = [
    path('api/rating/', views.RatingListCreate.as_view() ),
]