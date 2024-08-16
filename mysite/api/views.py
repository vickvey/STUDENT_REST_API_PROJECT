from django.shortcuts import render
from rest_framework.generics import (
    ListCreateAPIView, 
    RetrieveUpdateDestroyAPIView
)
from api import models, serializers

# List and create student records
class StudentListCreate(ListCreateAPIView):
    queryset = models.Student.objects.all()
    serializer_class = serializers.StudentSerializer

# Retrieve, update, and delete a student record
class StudentRetrieveUpdateDestroy(RetrieveUpdateDestroyAPIView):
    queryset = models.Student.objects.all()
    serializer_class = serializers.StudentSerializer
    lookup_field = 'roll_number'