from django.shortcuts import render, redirect
from crud_app.models import Student

# Create Function
def createpage(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        age = request.POST.get('age')
        email = request.POST.get('email')
        
        Student.objects.create(
            name=name,
            age=age,
            email=email,
        )
        
        return redirect('readpage')
    
    return render(request, 'create.html')

# Read Function
def readpage(request):
    Students = Student.objects.all()
    return render(request, 'read.html', {'studentsssss': Students})



# Update Function
def updatepage(request, id=id):
    student = Student.objects.get(id=id)
    
    if request.method == 'POST':
        student.name = request.POST.get('name')
        student.age = request.POST.get('age')
        student.email = request.POST.get('email')
        student.save()
        
        return redirect('readpage')
    
    return render(request, 'update.html' , {'student': student})


# Delete Function
def deletepage(request, id=id):
    student = Student.objects.get(id=id)
    student.delete()
    return redirect('readpage')
