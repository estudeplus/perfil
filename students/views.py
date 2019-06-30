from django.shortcuts import render, redirect, get_object_or_404
from .models import Student
from .forms import StudentForm
from rest_framework.generics import GenericAPIView
from rest_framework.mixins import UpdateModelMixin
from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from .serializers import StudentPreRegisterSerializer, StudentRegisterSerializer, StudentSerializer, StudentUpdateSerializer
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