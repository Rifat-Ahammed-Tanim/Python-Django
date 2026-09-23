from django.shortcuts import render, redirect
from authapp.models import User
from django.contrib.auth import authenticate, login, logout

# Register view
def register(request):

    if request.method == 'POST':

        name = request.POST.get('name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        

        User.objects.create_user(
            email=email,
            password=password
        )

        return redirect('login')

    return render(request, 'register.html')


# Login view
def login_view(request):
    if request.method == 'POST':

        email = request.POST.get('email')
        password = request.POST.get('password')

        user = authenticate(
            request,
            username=email,
            password=password
        )

        if user is not None:

            login(request, user)

            return redirect('home')

        return render(
            request,
            'login.html',
            {
                'error': 'Invalid email or password'
            }
        )

    return render(
        request,
        'login.html'
    )
    

# Logout view
def logout_view(request):
    logout(request)
    return redirect('login')

# Home view
def home(request):

    return render(request, 'home.html')