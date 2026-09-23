from django.urls import path
from authapp.views import register, login_view, logout_view, home


urlpatterns = [
    path('', register, name='register'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('home/', home, name='home'),
]