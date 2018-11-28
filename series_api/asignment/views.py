from django.shortcuts import render

# Create your views here.
from asignment.models import Assignment
from asignment.serializers import AssignmentSerializer
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.views import APIView

class AssignmentListCreate(generics.ListCreateAPIView):
  queryset = Assignment.objects.all()
  serializer_class = AssignmentSerializer

  def delete_assignment(request, userid, serieid):
    try:
      Assignment_for_deletion = Assignment.objects.filter(user_id=userid, serie_id=serieid)
      Assignment_for_deletion.delete()
      return Response("DELETED SUCCESSFULLY", status=status.HTTP_200_OK)
    except Assignment.DoesNotExist:
      return Response(status=status.HTTP_404_NOT_FOUND)


class AssignmentList(generics.ListAPIView):
  serializer_class = AssignmentSerializer

  def get_queryset(self):
    userid = self.kwargs['userid']
    return Assignment.objects.filter(user_id=userid)



#  Esta clase no esta en uso, la eliminacion esta en el delete_assignment de la clase AssignmentListCreate
class DeleteAssignment(generics.ListAPIView):

  serializer_class = AssignmentSerializer

  def get_queryset(self):
    userid = self.kwargs['userid']
    serieid = self.kwargs['serieid']
    try:
      Assignment_for_deletion = Assignment.objects.filter(user_id=userid, serie_id=serieid)
      Assignment_for_deletion.delete()
      return Response("DELETED SUCCESSFULLY", status=status.HTTP_200_OK)
    except Assignment.DoesNotExist:
      return Response(status=status.HTTP_404_NOT_FOUND)
