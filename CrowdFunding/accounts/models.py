from django.db import models
from django.contrib.auth.models import User
from django.db.models.aggregates import Max


class Reg(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    phone = models.IntegerField()
    profile = models.ImageField(upload_to='static/accounts/images/')
    fname = models.CharField(max_length=50)
    lname = models.CharField(max_length=50)
    password = models.CharField(max_length=80)


class Userinfo (models.Model) :
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    birth= models.DateField(),
    country = models.CharField(max_length=100),
    facebook_profile =  models.CharField(max_length=100)
