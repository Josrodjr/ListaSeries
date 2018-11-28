from django.urls import path
from django.conf.urls import url
from . import views

urlpatterns = [
    path('api/assignment/', views.AssignmentListCreate.as_view() ),
    url('^api/assignment/(?P<userid>.+)/$', views.AssignmentList.as_view()),
    path('api/deletion/<int:serieid>/<int:userid>/', views.AssignmentListCreate.delete_assignment ),
    # url('^api/assignment/(?P<serieid>.+)(?P<userid>.+)/$', views.AssignmentListCreate.delete ),
    # path('api/deletion//(?P<serieid>\d+)/(?P<userid>\d+)/$', views.AssignmentListCreate.delete_assignment ),
]