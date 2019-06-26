from django.contrib import admin
from django.urls import path, include
from students.views import StudentPreRegisterViewSet, StudentRegisterViewSet, StudentViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'pre-register', StudentPreRegisterViewSet, basename='pre-register')
router.register(r'register', StudentRegisterViewSet, basename='register')
router.register(r'students', StudentViewSet, basename='student')

urlpatterns = [
    path('', include(router.urls)),
    path('home/', include('students.urls')),
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls'))
]
