from django.db import models

# Create your models here.
class Employee(models.Model):
    name = models.CharField(max_length=20)
    emp_id = models.IntegerField(primary_key=True, auto_created=True)
    working_flag = models.BooleanField()
    company = models.CharField(max_length=20)
    