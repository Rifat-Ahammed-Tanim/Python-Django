from django.shortcuts import render, redirect
from crud.models import Student

# Create
def create(request):

    if request.method == 'POST':

        Student.objects.create(
            name=request.POST.get('name'),
            age=request.POST.get('age'),
            email=request.POST.get('email'),
            profile_image=request.FILES.get('profile_image')
        )

        return redirect('read')

    return render(request, 'create.html')

# Read
def read(request):

    students = Student.objects.all()

    return render(request, 'read.html', {
        'students': students
    })


# Update
def update(request, id):

    student = Student.objects.get(id=id)

    if request.method == 'POST':

        student.name = request.POST.get('name')
        student.age = request.POST.get('age')
        student.email = request.POST.get('email')

        if request.FILES.get('profile_image'):
            student.profile_image = request.FILES.get('profile_image')

        student.save()

        return redirect('read')

    return render(request, 'update.html', {
        'student': student
    })    


# Delete
def delete(request, student_id):

    student = Student.objects.get(id=student_id)
    student.delete()

    return redirect('read')