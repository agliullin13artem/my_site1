from django.db import models



class Employee(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    arrival_time = models.DateTimeField()
    departure_time = models.DateTimeField(null=True)