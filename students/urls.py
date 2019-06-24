from django.urls import path
from django.conf.urls import url
from students import views

urlpatterns = [
    path('', views.StudentList.as_view(), name='list_students'),
    path('new/', views.StudentCreate.as_view(), name='create_students'),
    path('update/<int:id>/', views.StudentUpdate.as_view(), name='update_student'),
    path('delete/<int:id>/', views.StudentDelete.as_view(), name='delete_student')

    """
    path('', views.list_students, name='list_students'),
    path('new/', views.create_student, name='create_students'),
    path('update/<int:id>/', views.update_student, name='update_student'),
    path('delete/<int:id>/', views.delete_student, name='delete_student')
    """
]