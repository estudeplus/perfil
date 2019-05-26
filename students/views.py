from django.shortcuts import render, redirect
from .models import Student
from .forms import StudentForm
import requests
import os

API_GATEWAY_EVENT = os.environ.get('API_GATEWAY_EVENT')


def list_students(request):
    students = Student.objects.all()
    return render(request, 'students.html', {'students': students})

def create_student(request):
    form = StudentForm(request.POST or None)

    if form.is_valid():
        student = form.save()
        data = {
          'uuid': student.uuid,
          'email': student.email,
          'senha': student.senha
        }
        requests.post(url = API_GATEWAY_EVENT, data = data)
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
