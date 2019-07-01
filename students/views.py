from django.shortcuts import render, redirect, get_object_or_404
from .models import Student, InstitutionalEmail
from .forms import StudentForm
from rest_framework.generics import GenericAPIView
from rest_framework.mixins import UpdateModelMixin
from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from .serializers import StudentPreRegisterSerializer, StudentRegisterSerializer, StudentSerializer, StudentUpdateSerializer, InstitutionalEmailSerializer
from django.urls import reverse_lazy

import requests
from requests.exceptions import RequestException

from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

class TableEmail():
    def save_table_email():
        email = Student.objects.values('student_id')
        id = Student.objects.values('id')
        p = InstitutionalEmail()
        for item in email:
            data = ""
            data = item.get("student_id", "")
            data = data + "@aluno.unb.br"
            p.address_email = data
        
        for item in id:
            data = ""
            data = item.get("id", "")
            data = "http://localhost:8002/students/" + str(data)
            p.body_email = data
        p.save()


class StudentPreRegisterViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentPreRegisterSerializer

    def create(self, request, *args, **kwargs):
        serializer = StudentPreRegisterSerializer(data=request.data) 

        if serializer.is_valid():
            serializer.save()
            TableEmail.save_table_email()
            return Response(serializer.data, status.HTTP_201_CREATED)

class StudentRegisterViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentRegisterSerializer

    def get_object(self):
        student_id = self.request.data['student_id']
        student = get_object_or_404(Student, student_id=student_id)
        return student
    
    def create(self, request, *args, **kwargs):
        student = self.get_object()
        serializer = StudentRegisterSerializer(student, data=request.data) 

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status.HTTP_201_CREATED)

class StudentViewSet(viewsets.ViewSet):

    queryset = Student.objects.all()
    serializer_class = StudentUpdateSerializer
    
    def list(self, request):
        queryset = Student.objects.all()
        serializer = StudentSerializer(queryset, many=True)
        return Response(serializer.data)
    
    def retrieve(self, request, pk=None):
        queryset = Student.objects.all()
        student = get_object_or_404(queryset, pk=pk)
        serializer = StudentSerializer(student)
        return Response(serializer.data)

    def perform_update(self, serializer):
        serializer.save()

    def perform_destroy(self, instance):
        instance.delete()

    def update(self, request, pk=None):
        queryset = Student.objects.all()
        student = get_object_or_404(queryset, pk=pk)
        serializer = StudentUpdateSerializer(student, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)

        if getattr(student, '_prefetched_objects_cache', None):
            # If 'prefetch_related' has been applied to a queryset, we need to
            # forcibly invalidate the prefetch cache on the instance.
            student._prefetched_objects_cache = {}

        return Response(serializer.data)

    def destroy(self, request, pk=None):
        queryset = Student.objects.all()
        student = get_object_or_404(queryset, pk=pk)
        self.perform_destroy(student)
        return Response(status=status.HTTP_204_NO_CONTENT)


class InstitutionalEmailViewSet(viewsets.ModelViewSet):

    queryset = InstitutionalEmail.objects.all()
    serializer_class = InstitutionalEmailSerializer