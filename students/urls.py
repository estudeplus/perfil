from django.urls import path
from .views import list_students, create_student, update_student, delete_student

urlpatterns = [
    path('', list_students, name='list_students'),
    path('new/', create_student, name='create_students'),
    path('update/<int:id>/', update_student, name='update_student'),
    path('delete/<int:id>/', delete_student, name='delete_student')
]