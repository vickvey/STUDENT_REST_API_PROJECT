from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from api.models import Student
from api.serializers import StudentSerializer

class StudentAPITestCase(TestCase):
    def setUp(self):
        # Initialize APIClient
        self.client = APIClient()
        
        # Create initial students in the test database
        self.student1 = Student.objects.create(roll_number=1, name='Alphonso Barbosa', major='CSE')
        self.student2 = Student.objects.create(roll_number=2, name='Bob Chaudhary', major='CIV')
        self.student3 = Student.objects.create(roll_number=3, name='Charlotte Dhawan', major='ECE')
        
        # Define URLs
        self.list_create_url = '/api/students/'
        self.detail_url = f'/api/students/{self.student1.roll_number}/'
        
    def test_student_list(self):
        # Test GET request to list all students
        response = self.client.get(self.list_create_url)
        students = Student.objects.all()
        serializer = StudentSerializer(students, many=True)
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, serializer.data)
    
    def test_student_create(self):
        # Test POST request to create a new student
        data = {'roll_number': 7, 'name': 'Alice Johnson', 'major': 'MEC'}
        response = self.client.post(self.list_create_url, data, format='json')
        
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Student.objects.count(), 4)  # Should be 4 now
        self.assertEqual(Student.objects.get(roll_number=7).name, 'Alice Johnson')
    
    def test_student_retrieve(self):
        # Test GET request to retrieve a specific student
        response = self.client.get(self.detail_url)
        student = Student.objects.get(roll_number=self.student1.roll_number)
        serializer = StudentSerializer(student)
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, serializer.data)
    
    def test_student_update(self):
        # Test PATCH request to update a specific student
        data = {'name': 'Updated Name'}
        response = self.client.patch(self.detail_url, data, format='json')
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Student.objects.get(roll_number=self.student1.roll_number).name, 'Updated Name')
    
    def test_student_delete(self):
        # Test DELETE request to remove a specific student
        delete_url = f'/api/students/{self.student1.roll_number}/'
        response = self.client.delete(delete_url)
        
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Student.objects.filter(roll_number=self.student1.roll_number).count(), 0)
    
    def test_student_retrieve_not_found(self):
        # Test GET request to retrieve a non-existent student
        response = self.client.get('/api/students/999/')
        
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
