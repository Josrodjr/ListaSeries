from django.urls import path
from django.conf.urls import url
from . import views

urlpatterns = [
    path('api/assignment/', views.AssignmentListCreate.as_view() ),
    url('^api/assignment/(?P<userid>.+)/$', views.AssignmentList.as_view()),
]