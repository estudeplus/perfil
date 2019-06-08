from rest_framework import serializers
from .models import Student

class StudentPreRegisterSerializer(serializers.ModelSerializer):
    class Meta:

        model = Student
        fields = ('matricula',)

class StudentRegisterSerializer(serializers.ModelSerializer):
    class Meta:

        model = Student
        fields = ('matricula', 'nome', 'email', 'senha')