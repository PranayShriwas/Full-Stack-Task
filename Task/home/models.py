from django.db import models

# Create your models here


class Registration(models.Model):
    Name = models.CharField(max_length=50)
    Phone = models.CharField(max_length=50, unique=True)
    Email = models.EmailField(max_length=254, unique=True)
    Password = models.CharField(max_length=50)
    Company = models.CharField(max_length=50)

    def __str__(self):
        return self.Name
