from django.urls import path
from crud.views import create, read, delete, update


urlpatterns = [
    path('', create, name='create'),
    path('read/', read, name='read'),
    path('update/<int:id>/', update, name='update'),
    path('delete/<int:student_id>/', delete, name='delete')
]