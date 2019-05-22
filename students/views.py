from django.shortcuts import render, redirect
from .models import Student
from .forms import StudentForm

def list_students(resquest):
    students = Student.objects.all()
    return render(resquest, 'students.html', {'students': students})

def create_student(resquest):
    form = StudentForm(resquest.POST or None)

    if form.is_valid():
        form.save()
        return redirect('list_students')
    
    return render(resquest, 'student-form.html', {'form': form})

def update_student(resquest, id):
    student = Student.objects.get(id=id)
    form = StudentForm(resquest.POST or None, instance=student)

    if form.is_valid():
        form.save()
        return redirect('list_students')

    return render(resquest, 'student-form.html', {'form': form}, {'student': student})