from django.db import models

# Create your models here.

class Student(models.Model):
    image         = models.ImageField()
    firstname     = models.CharField(max_length=255)
    lastname      = models.CharField(max_length=255)
    email         = models.EmailField(max_length=255)
    adm_no        = models.CharField(max_length=255)
    grade         = models.CharField(max_length=255)
    status        = models.CharField(max_length=255)
    date_joined   = models.DateField(max_length=255)
    
    def __str__(self):
        return self.firstname


