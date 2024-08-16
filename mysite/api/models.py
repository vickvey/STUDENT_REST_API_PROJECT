from django.db import models

# Create your models here.
class Student(models.Model):
    MAJORS=(
        ('CSE', 'Computer Science'),
        ('ECE', 'Electronics and Communication'),
        ('CIV', 'Civil Engineering'),
        ('MEC', 'Mechanical Engineering'),
    )
    name=models.CharField(max_length=100)
    roll_number=models.IntegerField(unique=True)
    major=models.CharField(max_length=3, choices=MAJORS)

    def __str__(self):
        return f'{self.name}_{self.major}'