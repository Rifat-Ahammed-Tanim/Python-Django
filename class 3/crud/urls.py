from django.urls import path
from crud.views import *

urlpatterns =[
    path('', homepage, name='homepage'),
    path('read/', readpage, name='asdfasdfad'),
    
]