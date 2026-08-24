from django.urls import path
from crud_app.views import *

urlpatterns = [
    path('create/', createpage, name='createpage'),
    path('', readpage, name='readpage'),
    path('update/<int:id>/', updatepage, name='updatepage'),
    path('delete/<int:id>/', deletepage, name='deletepage')
    
]