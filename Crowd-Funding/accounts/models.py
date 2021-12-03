from django.db import models
from django.contrib.auth.models import User
from django.db.models.aggregates import Max

class Reg(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE ),
    phone =models.IntegerField(),
    profile=models.ImageField(),
    firstName= models.CharField(max_length=100 ),
    lastName = models.CharField(max_length=100),
    
<<<<<<< HEAD
    
class Userinfo (models.Model) :
    user = models.ForeignKey(User, on_delete=models.CASCADE),
=======
    user_id =models.ForeignKey(User,on_delete=models.CASCADE , default=None)
    phone =models.IntegerField()
    profile=models.ImageField(default=None)
    
    
class Userinfo (models.Model) :
    user = models.ForeignKey(User, on_delete=models.CASCADE)
>>>>>>> 4dfdc7fcbba1fb6c58b2f2ad419064b3e21c7d5d
    birth= models.DateField(),
    country = models.CharField(max_length=100),
    facebook_profile =  models.CharField(max_length=100)
