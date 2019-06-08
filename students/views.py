from django.shortcuts import render, redirect, get_object_or_404
from .models import Student
from .forms import StudentForm
from rest_framework import viewsets, status
from rest_framework.response import Response
from .serializers import StudentPreRegisterSerializer, StudentRegisterSerializer

class StudentPreRegisterViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentPreRegisterSerializer

class StudentRegisterViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentRegisterSerializer

    def get_object(self):
        matricula = self.request.data['matricula']
        student = get_object_or_404(Student, matricula=matricula)
        return student
    
    def create(self, request, *args, **kwargs):
        student = self.get_object()
        serializer = StudentRegisterSerializer(student, data=request.data) 

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status.HTTP_201_CREATED)

def list_students(request):
    students = Student.objects.all()
    return render(request, 'students.html', {'students': students})

def create_student(request):
    form = StudentForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('list_students')
    
    return render(request, 'student-form.html', {'form': form})

def update_student(request, id):
    student = Student.objects.get(id=id)
    form = StudentForm(request.POST or None, instance=student)

    if form.is_valid():
        form.save()
        return redirect('list_students')

    return render(request, 'student-form.html', {'form': form, 'student': student})

def delete_student(request, id):
    student = Student.objects.get(id=id)

    if request.method == 'POST':
        student.delete()
        return redirect('list_students')

    return render(request, 'confirm_delete.html', {'student': student})