from django.db import models

# ORM Object-Relational Mapping
class Student(models.Model):
    name = models.CharField(max_length=255)
    age = models.IntegerField()
    email = models.EmailField()
