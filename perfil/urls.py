from django.contrib import admin
from django.urls import path, include
from students.views import StudentViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'students', StudentViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('home/', include('students.urls')),
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls'))
]
