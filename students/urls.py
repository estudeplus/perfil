from django.urls import path
from .views import create_student, list_students, update_student

urlpatterns = [
    path('', list_students, name='list_students'),
    path('new/', create_student, name='create_students'),
    path('update/<int:id>/', update_student, name='update_student')
]