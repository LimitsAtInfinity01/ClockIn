# Forms needed
# Register Employee
# Register Admin
# Clock in and out

from django import forms

class RegisterEmployeeForm(forms.Form):
    name = forms.CharField(label="Enter your name", max_length=32)
    lastName = forms.CharField(label="Enter your last name", max_length=32)
    username = forms.CharField(label="Enter your username", max_length=32)

class clockInOutForm(forms.Form):
    timeIn = forms.TimeField()
    timeOut = forms.TimeField()
