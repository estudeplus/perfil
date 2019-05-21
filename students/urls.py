from django.urls import path
from .views import create_student

urlpatterns = [
    path('new/', create_student, name='create_students')
]