# Forms needed
# Register Employee
# Register Admin
# Clock in and out
from django import forms
from django.forms import ModelForm
from clockInApp.models import Employee, Times, Admins
from django.contrib.auth.hashers import make_password

class RegisterEmployeeForm(forms.Form):
    name = forms.CharField(max_length=32)
    lastName = forms.CharField(max_length=32)
    username = forms.CharField(max_length=32)
    password = forms.CharField(max_length=128)

class AdminsForm(ModelForm):
    name = forms.CharField(max_length=32)
    lastName = forms.CharField(max_length=32)
    username = forms.CharField(max_length=32)
    password = forms.CharField(max_length=128)

class ClockInForm(forms.Form):
    username = forms.CharField(max_length=32)
    password = forms.CharField(max_length=128)

class ClockOutForm(forms.Form):
    username = forms.CharField(max_length=128)
    password = forms.CharField(max_length=128)

class ReportForm(forms.Form):
    username = forms.CharField(max_length=32)
    password = forms.CharField(max_length=128)


