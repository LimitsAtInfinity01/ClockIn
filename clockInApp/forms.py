# Forms needed
# Register Employee
# Register Admin
# Clock in and out
from django import forms
from django.forms import ModelForm
from clockInApp.models import Employee, Times, Admins
from django.contrib.auth.hashers import make_password

class RegisterEmployeeForm(forms.Form):
    name = forms.CharField(max_length=32, widget=forms.TextInput(attrs={'class':'w3-input w3-border'}))
    lastName = forms.CharField(max_length=32, widget=forms.TextInput(attrs={'class':'w3-input w3-border'}))
    username = forms.CharField(max_length=32, widget=forms.TextInput(attrs={'class':'w3-input w3-border'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'w3-input w3-border'}))

class AdminsForm(ModelForm):
    name = forms.CharField(max_length=32, widget=forms.TextInput(attrs={'class':'w3-input w3-border'}))
    lastName = forms.CharField(max_length=32, widget=forms.TextInput(attrs={'class':'w3-input w3-border'}))
    username = forms.CharField(max_length=32, widget=forms.TextInput(attrs={'class':'w3-input w3-border'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'w3-input w3-border'}))

class ClockInForm(forms.Form):
    username = forms.CharField(max_length=32, widget=forms.TextInput(attrs={'class':'w3-input w3-border'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'w3-input w3-border'}))

class ClockOutForm(forms.Form):
    username = forms.CharField(max_length=128, widget=forms.TextInput(attrs={'class':'w3-input w3-border'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'w3-input w3-border'}))

class ReportForm(forms.Form):
    username = forms.CharField(max_length=32, widget=forms.TextInput(attrs={'class':'w3-input w3-border'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'w3-input w3-border'}))


