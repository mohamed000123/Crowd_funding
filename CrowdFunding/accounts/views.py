from django.shortcuts import redirect, render 
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login as auth_login
from django.contrib.auth.decorators import login_required
from projects.models import Projects, ProjectRating
from accounts.models import User, Userinfo, Reg

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login as auth_login

from verify_email.email_handler import send_verification_email

from django.http import HttpResponse  
from django.shortcuts import render, redirect  
from django.contrib.auth import login, authenticate, get_user_model
from .forms import SignupForm  
from django.contrib.sites.shortcuts import get_current_site  
from django.utils.encoding import force_bytes, force_text  
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode  
from django.template.loader import render_to_string  
from .token import account_activation_token  
from django.contrib.auth.models import User  
from django.core.mail import EmailMessage  


# def sign(request):
#     if request.user.is_authenticated:
#         return redirect('/pro')
#     form = signupForm()
#     if request.method == "POST":
#         form = signupForm(request.POST)
#         if form.is_valid():
#             user=form.save()
#             Reg.objects.create(user=user, phone=request.POST["phone"], profile=request.FILES.get("pic"), fname=request.POST['first_name'], lname=request.POST['last_name'], password=request.POST['password1'])
#             auth_login(request, user)
#             return redirect('/pro')
#     return render(request, 'accounts/signup.html', {'form': form})

def signup(request):  
    if request.method == 'POST':  
        form = SignupForm(request.POST)  
        if form.is_valid():  
            # save form in the memory not in database  
            user = form.save(commit=False)  
            user.is_active = False  
            user.save()
            Reg.objects.create(user=user, phone=request.POST["phone"], profile=request.FILES.get("pic"), fname=request.POST['first_name'], lname=request.POST['last_name'], password=request.POST['password1'])
            # to get the domain of the current site  
            current_site = get_current_site(request)  
            mail_subject = 'Activation link has been sent to your email id'  
            message = render_to_string('acc_active_email.html', {  
                'user': user,  
                'domain': current_site.domain,  
                'uid':urlsafe_base64_encode(force_bytes(user.pk)),  
                'token':account_activation_token.make_token(user),  
            })  
            to_email = form.cleaned_data.get('email')  
            email = EmailMessage(  
                        mail_subject, message, to=[to_email]  
            )  
            email.send()  
            return HttpResponse('Please confirm your email address to complete the registration')  
    else:  
        form = SignupForm()  
    return render(request, 'accounts/signup.html', {'form': form})   


def activate(request, uidb64, token):  
    User = get_user_model()  
    try:  
        uid = force_text(urlsafe_base64_decode(uidb64))  
        user = User.objects.get(pk=uid)  
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):  
        user = None  
    if user is not None and account_activation_token.check_token(user, token):  
        user.is_active = True  
        user.save()  
        # return HttpResponse('Thank you for your email confirmation. Now you can login your account.')
        return redirect("/accounts/login")
    else:  
        return HttpResponse('Activation link is invalid!')  
  


@login_required
def profile (request) :
    if request.user.is_authenticated:
        User = request.user 
        UserId= request.user.id 
        profile=Reg.objects.get(user_id=UserId)
        UserProjects=Projects.objects.filter(user=UserId).all()
        UserDonations=ProjectRating.objects.filter(user=UserId).all()
        return render(request, 'accounts/profile.html',{"user":User , "UserProjects":UserProjects , "donations" :  UserDonations ,"profile":profile})
    else:
        return redirect("/accounts/login")



@login_required
def edit(request):
    if request.method == "POST":
        User = request.user 
        if request.POST['fname']:
            Reg.objects.filter(user=User).update(fname=request.POST['fname'])
        if request.POST['lname']:
            Reg.objects.filter(user=User).update(lname=request.POST['lname'])
        if request.POST['phone']:
            Reg.objects.filter(user=User).update(phone=request.POST['phone'])
        if request.FILES['image']:
            reg = Reg.objects.get(user=User)
            Reg.objects.create(user=request.user, phone=reg.phone, profile=request.FILES.get("image"), fname=reg.fname, lname=reg.lname)
            reg.delete()
    return redirect("/accounts/profile")
   
@login_required
def delete (request) :
    UserId= request.user.id
    if  request.POST["password1"] == Reg.objects.get(user=UserId).password:
        User.objects.filter(id=UserId).delete()
        return redirect("/accounts/logout")
    else:
        wrongpassword = "password is not confirmed"
        return render(request, 'accounts/profile.html',{"wrongpassword" : wrongpassword })
 

@login_required
def add (request) :
    print(request.POST)
    Userinfo.objects.create(user=request.user,birth=request.POST["birthday"],country=request.POST["country"],facebook_profile=request.POST["facebookprofile"])
    return redirect("/accounts/profile")
     
      
        
        
        
        
                                                  

 
