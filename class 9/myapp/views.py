from django.shortcuts import render, redirect
from myapp.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required


@login_required
def home(request):
    return render(request, 'home.html')

# register Function
def register_view(request):
    
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        
        
        User.objects.create_user(
            # name=name,
            email=email,
            password=password,            
        )
        
        return redirect('login')
    
    return render(request, 'register.html')


# login Function
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
        
        return render(request, 'login.html', {'error': 'Invalid email or password'})
    
    return render(request, 'login.html')


# logout Function
def logout_view(request):
    logout(request)
    return redirect('login')