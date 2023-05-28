
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from .serializers import *
from django.urls import path,include
from .views import *
from drf_yasg import openapi
from rest_framework import permissions
from drf_yasg.views import get_schema_view

schema_view = get_schema_view(
    openapi.Info(
        title="Your API",
        default_version='v1',
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('student/',StudentViewSet.as_view({'get':'list','post':'create'})),
    path('student/<int:pk>/',StudentViewSet.as_view({'get':'retrieve','put':'update','delete':'destroy'})),
    path('teacher/',TeacherViewSet.as_view({'get':'list','post':'create'})),
    path('teacher/<int:pk>/',TeacherViewSet.as_view({'get':'retrieve','put':'update','delete':'destroy'})),
    path('course/',CourseViewSet.as_view({'get':'list','post':'create'})),
    path('course/<int:pk>/',CourseViewSet.as_view({'get':'retrieve','put':'update','delete':'destroy'})),
    path('grade/',GradeViewSet.as_view({'get':'list','post':'create'})),
    path('grade/<int:pk>/',GradeViewSet.as_view({'get':'retrieve','put':'update','delete':'destroy'})),

   
]
urlpatterns += staticfiles_urlpatterns()
