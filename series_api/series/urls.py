from django.urls import path
from django.conf.urls import url
from . import views

urlpatterns = [
    path('api/series/', views.SerieListCreate.as_view() ),
    url('^api/series/(?P<serie_name>.+)/$', views.SeriesList.as_view()),
    url('^api/serie/byid/(?P<serieId>.+)/$', views.SerieListId.as_view()),
]