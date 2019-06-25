from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=100)
    student_id = models.CharField(max_length=10)
    email = models.EmailField(max_length=254)
    password = models.CharField(max_length=15)

    def __str__(self):
        return self.name
