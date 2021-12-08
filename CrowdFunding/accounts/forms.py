from django import forms
from django.contrib.auth import forms as myforms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import widgets


class SignupForm (UserCreationForm) :
    email = forms.EmailField(required=True)
    phone = forms.IntegerField()
    first_name = forms.CharField()
    last_name = forms.CharField()
    

    
    
 