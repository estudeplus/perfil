from django.urls import path
from django.conf.urls import url
from students import views

urlpatterns = [
    path('', views.StudentList.as_view(), name='list_students'),
    path('new/', views.StudentCreate.as_view(), name='create_students'),
    path('update/<int:pk>/', views.StudentUpdate.as_view(), name='update_student'),
    path('delete/<int:pk>/', views.StudentDelete.as_view(), name='delete_student')
]