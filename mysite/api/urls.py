from django.urls import path
from api import views

urlpatterns = [
    # For Creating Student and Getting a List of Students
    path('students/', views.StudentListCreate.as_view(), name='students-list'),
    
    # For Detailing, Updating and Deleting a Student Instance
    path('students/<int:roll_number>/', views.StudentRetrieveUpdateDestroy.as_view(), name='student-detail'),
]
