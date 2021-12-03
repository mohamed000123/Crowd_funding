from django.shortcuts import redirect, render 
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login as auth_login
from .forms import  signupForm
from .models import Reg
from django.contrib.auth.decorators import login_required
from projects.models import Projects , ProjectRating
from accounts.models import User , Userinfo

<<<<<<< HEAD

=======
>>>>>>> 4dfdc7fcbba1fb6c58b2f2ad419064b3e21c7d5d
def sign (request) :
    if request.user.is_authenticated:
        return redirect('/pro')
    form = signupForm()
    if request.method=="POST":
        form = signupForm(request.POST)
        if form.is_valid():
        
            user=form.save()
            Reg.objects.create(user=request.user , phone=request.POST["phone"],profile=request.FILES.get("profile"),firstName=request.POST["firstName"],lastName=request.POST["lastName"] )
            auth_login(request,user)
            return redirect('/pro')
    return render(request ,'accounts/signup.html',{'form' : form})
  


@login_required
def profile (request) :
    if request.user.is_authenticated:
<<<<<<< HEAD
        U = request.user 
        UserId= request.user.id 
      
        # firstName=Reg.objects.get(user_id=UserId).firstName
        # lastName=Reg.objects.get(user_id=UserId).lastName
        profile=Reg.objects.get(user_id=UserId).profile  
        UserProjects=Projects.objects.filter(user=UserId).all()
        UserDonations=ProjectRating.objects.filter(user=UserId).all()
        return render(request, 'accounts/profile.html',{"user":U, "UserProjects":UserProjects , "donations" :  UserDonations ,"profile":profile})
=======
        
        User = request.user 
        UserId= request.user.id 
        profile=Reg.objects.get(user_id=UserId).profile 
        UserProjects=Projects.objects.filter(user=UserId).all()
        UserDonations=ProjectRating.objects.filter(user=UserId).all()
        return render(request, 'accounts/profile.html',{"user":User , "UserProjects":UserProjects , "donations" :  UserDonations ,"profile":profile})
>>>>>>> 4dfdc7fcbba1fb6c58b2f2ad419064b3e21c7d5d
    else:
        return redirect("/accounts/login")



@login_required
def edit (request) :
    if request.method == "POST":
<<<<<<< HEAD
        Reg.objects.filter(user_id=request.user.id ).update(phone=request.POST["phone"],profile=request.POST["profile"],
        firstName=request.POST["firstName"],lastName=request.POST["lastName"])
        # User = request.user 
        # UserId= request.user.id 
        # if  User.objects.filter(password=request.POST["password"]):
        #     if  request.POST["password1"]==request.POST["password2"] :
        #         User.objects.filter(userid=UserId).update(username=request.POST["username"],
        #         password=request.POST["password1"] )
        #     else: 
        #         wrongpassword = "password is not confirmed"
        #         return render(request, 'accounts/profile.html',{"wrongpassword" : wrongpassword })                                         
        # else: 
        #     wrongpassword = "wrong password "
        #     return render(request, 'accounts/profile.html',{"wrongpassword" : wrongpassword })                                         
   
            
       
            
      
@login_required
def delete (request) :
    UserId= request.user.id
    if  request.POST["password1"]==request.POST["password2"] : 
        User.objects.filter(id=UserId).delete()
        return redirect("/accounts/logout")
    else: 
        wrongpassword = "password is not confirmed"
        return render(request, 'accounts/profile.html',{"wrongpassword" : wrongpassword })                                         
    
=======
        User = request.user 
        UserId= request.user.id  
      
        if  request.POST["password1"]==request.POST["password2"] :
            User.objects.filter(userid=UserId).update(username=request.POST["username"],
            password=request.POST["password1"] )
            
        else: 
             wrongpassword = "password is not confirmed"
             return render(request, 'accounts/profile.html',{"wrongpassword" : wrongpassword })                                         
   
@login_required
def delete (request) :
     UserId= request.user.id
        
     User.objects.filter(id=UserId).delete()
     return redirect("/accounts/logout")
 
>>>>>>> 4dfdc7fcbba1fb6c58b2f2ad419064b3e21c7d5d

@login_required
def add (request) :
    print(request.POST)
    Userinfo.objects.create(user=request.user,birth=request.POST["birthday"],country=request.POST["country"],facebook_profile=request.POST["facebookprofile"])
    return redirect("/accounts/profile")
     
      
        
        
        
        
                                                  

 
