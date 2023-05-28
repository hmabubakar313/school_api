
from django.contrib import admin
from .serializers import *
from .views import *
from django.urls import path,include
from rest_framework import routers

router = routers.DefaultRouter()

router.register('student', StudentViewSet, basename='student')
router.register('teacher', TeacherViewSet, basename='teacher')
router.register('grade', GradeViewSet, basename='grade')
router.register('course', CourseViewSet, basename='course')

urlpatterns = [
    path('', include(router.urls)),
    path('swagger/', get_swagger_view(title='School API')),
   
]
