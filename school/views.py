from django.shortcuts import render
from .models import * 
from .serializers import *
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework_swagger.views import get_swagger_view
from rest_framework.generics import ListAPIView, RetrieveAPIView, CreateAPIView, UpdateAPIView, DestroyAPIView
from django.shortcuts import get_object_or_404
from rest_framework import permissions
from rest_framework.pagination import PageNumberPagination
from django_filters import rest_framework as filters
schema_view = get_swagger_view(title='School API')





class StudentViewSet(viewsets.ViewSet):
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_fields = ('name', 'email')

    
    
    # user pagination
    def list(self, request):
        paginator = PageNumberPagination()
        paginator.page_size = 5
        queryset = Student.objects.all()
        result_page = paginator.paginate_queryset(queryset, request)
        serializer = StudentSerializer(result_page, many=True)
        return paginator.get_paginated_response(serializer.data)    
   
   
    def create(self, request):
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'Data Created'})
        return Response(serializer.errors)
    
    
    def retrieve(self, request, pk=None):
        queryset = Student.objects.all()
        student = get_object_or_404(queryset, pk=pk)
        serializer = StudentSerializer(student)
        return Response(serializer.data)
    
    def update(self, request, pk=None):
        student = Student.objects.get(pk=pk)
        serializer = StudentSerializer(student, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'Data Updated'})
        return Response(serializer.errors)
    
    
    def destroy(self, request, pk=None):
        student = Student.objects.get(pk=pk)
        student.delete()
        return Response({'msg':'Data Deleted'})




class TeacherViewSet(viewsets.ViewSet):
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_fields = ('name', 'email')
      # user pagination
    def list(self, request):
        paginator = PageNumberPagination()
        paginator.page_size = 5
        queryset = Teacher.objects.all()
        result_page = paginator.paginate_queryset(queryset, request)
        serializer = TeacherSerializer(result_page, many=True)
        return paginator.get_paginated_response(serializer.data)
    
    def create(self,request):
        serializer = TeacherSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'Data Created'})
        return Response(serializer.errors)
    
    def retrieve(self,request,pk=None):
        queryset = Teacher.objects.all()
        teacher = get_object_or_404(queryset, pk=pk)
        serializer = TeacherSerializer(teacher)
        return Response(serializer.data)
    
    def update(self,request,pk=None):
        teacher = Teacher.objects.get(pk=pk)
        serializer = TeacherSerializer(teacher, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'Data Updated'})
        return Response(serializer.errors)
    
    def destroy(self,request,pk=None):
        teacher = Teacher.objects.get(pk=pk)
        teacher.delete()
        return Response({'msg':'Data Deleted'})
    



class CourseViewSet(viewsets.ViewSet):
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_fields = ('name', 'duration')
    
    
    # user pagination
    def list(self,request):
        paginator = PageNumberPagination()
        paginator.page_size = 5
        queryset = Course.objects.all()
        result_page = paginator.paginate_queryset(queryset, request)
        serializer = CourseSerializer(result_page, many=True)
        return paginator.get_paginated_response(serializer.data)
    
    def create(self,request):
        serializers = CourseSerializer(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response({'msg':'Data Created'})
        return Response(serializers.errors)
    
    def  retrieve(self,request,pk=None):
        queryset = Course.objects.all()
        course = get_object_or_404(queryset, pk=pk)
        serializer = CourseSerializer(course)
        return Response(serializer.data)
    
    def update(self,request,pk=None):
        course = Course.objects.get(pk=pk)
        serializer = CourseSerializer(course, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'Data Updated'})
        return Response(serializer.errors)
    
    def destroy(self,request,pk=None):
        course = Course.objects.get(pk=pk)
        course.delete()
        return Response({'msg':'Data Deleted'})
    


class GradeViewSet(viewsets.ViewSet):
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_fields = ('course', 'student')
    
    
    def list(self,request):
        paginator = PageNumberPagination()
        paginator.page_size = 5
        queryset = Grade.objects.all()
        result_page = paginator.paginate_queryset(queryset, request)
        serializer = GradeSerializer(result_page, many=True)
        return paginator.get_paginated_response(serializer.data)
    
    def create(self,request):
        serializer = GradeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'Data Created'})
        return Response(serializer.errors)
    
    
    def update(self,request,pk=None):
        queryset = Grade.objects.all()
        grade = get_object_or_404(queryset, pk=pk)
        serializer = GradeSerializer(grade, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'Data Updated'})
        return Response(serializer.errors)
    
    def destroy(self,request,pk=None):
        queryset = Grade.objects.all()
        grade = get_object_or_404(queryset, pk=pk)
        grade.delete()
        return Response({'msg':'Data Deleted'})
    
    