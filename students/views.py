from django.shortcuts import render
from .models import Student
from .forms import StudentForm

def create_student(resquest):
    form = StudentForm(resquest.POST or None)

    if form.is_valid():
        form.save()