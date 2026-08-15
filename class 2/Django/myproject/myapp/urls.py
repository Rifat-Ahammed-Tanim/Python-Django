from django.urls import path
from myapp.views import *

urlpatterns = [
    path('', index, name='homepage'),
    path('about/', about, name='aboutpage'),
]