from rest_framework import serializers
from .models import Student

class StudentPreRegisterSerializer(serializers.ModelSerializer):
    class Meta:

        model = Student
        fields = ('student_id',)

class StudentRegisterSerializer(serializers.ModelSerializer):
    class Meta:

        model = Student
        fields = ('student_id', 'name', 'email', 'password')