from rest_framework import serializers
from .models import Student, InstitutionalEmail

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

class InstitutionalEmailSerializer(serializers.ModelSerializer):
    class Meta:

        model = InstitutionalEmail
        fields = ('address_email', 'title_email', 'body_email')