from django.shortcuts import render , redirect
from .forms import SignupForm , ActivateUser
from .models import Profile
from django.core.mail import send_mail

# Create your views here.

def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            form.save()
            
            profile = Profile.objects.get(user__username=username)
            
        # send email 
            send_mail(
                subject='Activate Your Account',
                message= f'Welcome {username} , use this code {profile.code} to activate your account',
                from_email='ghayath94sh@gmail.com',
                recipient_list=[email],
                fail_silently=False,
            )
            return redirect(f'/accounts/{username}/activate')        
    else:
        form = SignupForm()
        
    return render(request,'accounts/signup.html',{'form':form})



def activate_user(request,username):
    profile = Profile.objects.get(user__username=username)
    if request.method == 'POST':
        form = ActivateUser(request.POST)
        if form.is_valid():
            code = form.cleaned_data['code']
            if code == profile.code : 
                profile.code = ''
                profile.code_used = True 
                profile.save()
                return redirect('/accounts/login')
    else:
        form = ActivateUser()
    return render(request,'accounts/activate.html',{'form':form})