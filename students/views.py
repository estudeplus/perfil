from django.shortcuts import render
from .models import Student

def create_student(resquest):
    form = StudentForm(resquest.POST or None)

    if form.is_valid():
        form.save()

    return render(request, 'student-form.html', {'form': form})