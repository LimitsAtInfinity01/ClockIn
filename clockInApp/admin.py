from django.contrib import admin
from .models import Employee, Times, Admins

# Register your models here.
admin.site.register(Employee)
admin.site.register(Times)
admin.site.register(Admins)