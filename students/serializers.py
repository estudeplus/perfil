from rest_framework import serializers
from .models import Student

class StudentLoginSerializer(serializers.ModelSerializer):
    class Meta:

        model = Student
        fields = ('id', 'email', 'senha')

class StudentFieldsSerializer(serializers.ModelSerializer):
    class Meta:

        model = Student
        fields = '__all__'