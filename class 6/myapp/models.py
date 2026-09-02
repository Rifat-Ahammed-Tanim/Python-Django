from django.db import models


class Student(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    email = models.EmailField()
    profile_image = models.ImageField(upload_to='profile_images/', null=True, blank=True)
    
    def __str__(self):
        return self.name
