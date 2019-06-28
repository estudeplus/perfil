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

class StudentSerializer(serializers.ModelSerializer):
    class Meta:

        model = Student
        fields = '__all__'

class StudentUpdateSerializer(serializers.ModelSerializer):
    class Meta:

        model = Student
        fields = ('name', 'email', 'password')