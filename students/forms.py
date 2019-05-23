from django import forms
from .models import Student

class StudentForm(forms.ModelForm):
    senha = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = Student
        fields = ['nome', 'matricula', 'email', 'senha']