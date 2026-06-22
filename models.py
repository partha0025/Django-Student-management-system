from django.db import models

class Student(models.Model):

    student_id = models.AutoField(primary_key=True)
    full_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    mobile = models.CharField(max_length=10)
    dob = models.DateField()
    gender = models.CharField(max_length=10)
    address = models.TextField()

    def __str__(self):
        return self.full_name
