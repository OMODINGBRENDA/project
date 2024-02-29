from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import Student, Teacher


# # Create your views here.
def home(request):
     return render(request,'home.html')

def about(request):
   return render(request,'about.html')
def contact(request):
    return render(request,'contact.html')

def login(request):
    return render(request,'login.html')
def logout(request):
    return render(request,'logout.html')
def service(request):
    return render(request,'service.html')
def students_list(request):
    student = Student.objects.all()
    return render(request,'students.html',{'student':student})
def teachers(request):
    teacher = Teacher.objects.all()
    return render(request,'teachers.html',{'teacherss':teacher})
