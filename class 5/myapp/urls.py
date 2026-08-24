from django.urls import path
from myapp.views import index, about, service


urlpatterns = [
    path('', index, name='index'),
    path('about/', about, name='about'),
    path('service/', service, name='service'),
]