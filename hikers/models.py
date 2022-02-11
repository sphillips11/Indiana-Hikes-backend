from django.db import models


class Hiker(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100, unique=True)
    username = models.CharField(max_length=100, unique=True)
    password = models.CharField(max_length=20)
    registered = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name