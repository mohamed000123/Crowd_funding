from django import forms
from django.contrib.auth import forms as myforms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import widgets

class signupForm (UserCreationForm) :
    email=forms.EmailField(  required=True)
    phone =forms.IntegerField()
    firstName=forms.CharField(max_length=100)
    lastName=forms.CharField(max_length=100)
    

    
    
 