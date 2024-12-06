from django.db import models

# Create your models here.
class Employee(models.Model):
    name = models.CharField(max_length=30)
    lastName = models.CharField(max_length=30)
    username = models.CharField(max_length=30)

    class Meta:
        db_table = "Employee"

class Admins(models.Model):
    name = models.CharField(max_length=30)
    username = models.CharField(max_length=30)


class times(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    timeIn = models.TimeField()
    timeOut = models.TimeField()