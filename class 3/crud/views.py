from django.shortcuts import render, redirect
from crud.models import *
from crud.urls import *

# Create
def homepage(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        age = request.POST.get("age")
    
        student = Student.objects.create(
            name = name,
            email = email,
            age = age,
        )
        student.save()
        return redirect("asdfasdfad")
    
    return render(request, 'index.html')

# Read
def readpage(request):
    student = Student.objects.all()
    return render(request, 'read.html', {'students': student})
