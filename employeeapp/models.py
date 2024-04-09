from django.db import models

# Create your models here.


class Employee(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    age = models.PositiveIntegerField()
    gender = models.CharField(max_length=10)
    phoneNo = models.CharField(max_length=20, blank=True)
    addressDetails = models.JSONField(default=dict)
    workExperience = models.JSONField(default=list)
    qualifications = models.JSONField(default=list)
    projects = models.JSONField(default=list)
    photo = models.TextField(blank=True)  # Base64 encoded image data

    def __str__(self):
        return self.name

