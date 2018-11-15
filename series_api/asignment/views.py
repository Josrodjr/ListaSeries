from django.shortcuts import render

# Create your views here.
from asignment.models import Assignment
from asignment.serializers import AssignmentSerializer
from rest_framework import generics

class AssignmentListCreate(generics.ListCreateAPIView):
  queryset = Assignment.objects.all()
  serializer_class = AssignmentSerializer


class AssignmentList(generics.ListAPIView):
  serializer_class = AssignmentSerializer

  def get_queryset(self):
    userid = self.kwargs['userid']
    return Assignment.objects.filter(user_id=userid)
