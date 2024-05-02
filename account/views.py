from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth import authenticate,login,logout
from django.core.mail import send_mail

from .forms import *
def user_login(request):
    error_msg = ''
    if request.method == 'POST':
        loginForm  = LoginForm(request.POST)
        if loginForm.is_valid():
            username = loginForm.cleaned_data['username']
            password = loginForm.cleaned_data['password']
            user = authenticate(username = username,password =password)
            if user:
                login(request, user)
                return redirect('home')
            else:
                error_msg = 'invalid username or password'
    else:
        loginForm  = LoginForm(request.POST)
    context  ={
        'loginForm': loginForm,
        'error_msg': error_msg,
    }
    return render(request,'account/login.html',context)
def user_logout(request):
    logout(request)
    return redirect('login')

def user_signup(request):
    error_msg = ''
    if request.method == 'POST':
        signupForm  = SignupForm(request.POST)
        if signupForm.is_valid():
           user = signupForm(commit=False)
           user.active = False
           user.save()
           subject = "Account Activation"
           from_email =None
           recipient_list = user.email
           send_mail(subject=subject, message, from_email, recipient_list)

            
