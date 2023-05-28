from django.db import models




class Student(models.Model):
    name = models.CharField(max_length=50)
    roll_number = models.IntegerField()
    dob = models.DateField()
    email = models.EmailField()
    phone = models.IntegerField()
    address = models.CharField(max_length=100)


class Teacher(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    phone = models.IntegerField()
    address = models.CharField(max_length=100)
    subject = models.CharField(max_length=50)
    salary = models.IntegerField()


class Course(models.Model):
    name = models.CharField(max_length=50)
    duration = models.IntegerField()
    fee = models.IntegerField()
    start_date = models.DateField()
    end_date = models.DateField()



class Grade(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    grade = models.CharField(max_length=50)
    date = models.DateField()