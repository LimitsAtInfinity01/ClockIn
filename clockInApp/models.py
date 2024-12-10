from django.db import models
from django.contrib.auth.hashers import make_password, check_password

# Create your models here.
class Employee(models.Model):
    name = models.CharField(max_length=32)
    lastName = models.CharField(max_length=32)
    username = models.CharField(max_length=32, unique=True)
    password = models.CharField(max_length=128)
    signedIn = models.BooleanField(default=False)

    def set_password(self, raw_password):
        self.password = make_password(raw_password)
    
    def check_password(self, raw_password):
        return check_password(raw_password, self.password)

    class Meta:
        db_table = "employee"

class Admins(models.Model):
    name = models.CharField(max_length=32)
    lastName = models.CharField(max_length=32)
    username = models.CharField(max_length=32, unique=True)
    password = models.CharField(max_length=128)

    def set_password(self, raw_password):
        self.password = make_password(raw_password)
    
    def check_password(self, raw_password):
        return check_password(raw_password, self.password)

    class Meta:
        db_table = "admins"

class Times(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    timeIn = models.TimeField()
    timeOut = models.TimeField(default=None, null=True)
    date = models.DateField(null=True, blank=True)
    def set_time_out(self, time):
        self.timeOut = time
    class Meta:
        db_table = "times"