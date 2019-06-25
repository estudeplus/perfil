from django.shortcuts import render, redirect, get_object_or_404
from .models import Student
from .forms import StudentForm
from rest_framework import viewsets, status
from rest_framework.response import Response
from .serializers import StudentPreRegisterSerializer, StudentRegisterSerializer
from django.urls import reverse_lazy

from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

class StudentPreRegisterViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentPreRegisterSerializer

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

class StudentForm(StudentForm):
    class Meta:
        model = Student
        fields = ['name', 'student_id', 'email', 'password']

class StudentList(ListView):
    model = Student

class StudentCreate(CreateView):
    model = Student
    fields = ['name','student_id','email','password']

    success_url = reverse_lazy('list_students')

class StudentUpdate(UpdateView):
    model = Student
    fields = ['name','email','password']

    success_url = reverse_lazy('list_students')

class StudentDelete(DeleteView):
    model = Student

    success_url = reverse_lazy('list_students')