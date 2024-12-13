from django.shortcuts import render
from django.http import HttpResponse
from .models import *
# Create your views here.
def home(request):
    students=Student.objects.all()
    return render(request,'home.html',{'students':students})

def student(request,student_id):
    student=Student.objects.get(id=student_id)
    return render(request,'student.html',{'student':student})
