from django.urls import path
from myapp.views import create, read, update, delete

urlpatterns = [
    path('', read, name='read'),
    path('create/', create, name='create'),
    path('update/<int:student_id>/', update, name='update'),
    path('delete/<int:student_id>/', delete, name='delete')
]