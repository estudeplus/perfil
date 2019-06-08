from django.contrib import admin
from django.urls import path, include
from students.views import StudentPreRegisterViewSet, StudentRegisterViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'pre-register', StudentPreRegisterViewSet)
router.register(r'register', StudentRegisterViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('home/', include('students.urls')),
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls'))
]
