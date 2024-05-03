from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout,get_user_model
from django.http import HttpResponse
from django.utils.http import urlsafe_base64_decode
from django.contrib.auth.tokens import default_token_generator
from django.contrib.sites.shortcuts import get_current_site  

from django.core.mail import send_mail
from .token import account_activation_token
from django.conf import settings
import os



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
    if request.method == 'POST':
        signupForm  = SignupForm(request.POST)
        if signupForm.is_valid():
            user = signupForm.save(commit=False)
            user.active = False
            user.save()
           
        # will be back ground task 
            while True:
               sent =   sent_activation(user)
               if sent:
                  break 
            return HttpResponse("email delivered")
    else:
         signupForm  = SignupForm()
    context = {
        'signupForm':signupForm,
        
    }
    return  render(request,'account/signup.html',context)  
def mailHtmlFormatter(title,subject,name,text,link):
    htmlContent  = """
        <!DOCTYPE html>
        <html lang="en">
        <head>
        <meta charset="UTF-8">
        <meta http-equiv="X-UA-Compatible" content="IE=edge">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>{title}</title>
        </head>

        <body style="font-family: 'Times New Roman', Times, serif;">
        <table cellpadding="0" cellspacing="0" border="0" align="center" style="background-color: rgb(217, 216, 216); margin: 4% 10%; border-bottom: outset 6px rgb(11, 125, 170); border-radius: 0 30px;">
            <tr>
                <td>
                    <div style="color: rgb(1, 101, 189); background-color: rgba(159, 214, 240, 0.863); padding: 1px 20px; border-bottom: inset 3px rgb(7, 111, 163); border-top-right-radius: 30px;">
                                <h2 >{subject}</h2>
                    </div>
                    <div style="padding: 5%;">
                                <p>Hello {name}, </p>
                                    <br>

                                <p>{text} Lorem ipsum dolor, sit amet consectetur adipisicing elit. Quos veniam dolorem aut quisquam placeat error, fugit iure vel maiores laborum necessitatibus similique itaque facilis saepe a recusandae ea ipsum quam.</p>
                                <a title="{title}" href="{link}" style="text-decoration: none; background-color: rgb(0, 136, 215); color: rgb(255, 255, 255); font-size: larger; margin: 5%; padding: 0.5% 3%;">{title}</a>

                        
                    </div>
                    <hr>
                    <h5 style="padding-left: 10px; width: 90%; text-align: center; font-style: italic; color: rgb(70, 80, 80);">From <i>JanPost:</i></h5>
                </td>
            </tr>
        </table>
        </body>
        </html>

 
    
    
    
    
    
    
    
    
    
    """
    return htmlContent
def sent_activation(request,user):
    token  = account_activation_token.make_token(user)
    current_site = get_current_site(request)  
    link = fr"https:{current_site.domain}/account/activate{user.id}/{token}"
    print("link token -------------------------------------------")
    print(link)
    try:
        subject = "Account Activation"
        title = "Activate"
        text = "Your account has been created! To start using it, you'll need to activate it. Simply click the link/button below to get started."
        htmlMessage = mailHtmlFormatter(title = title,subject= subject,name = user.username,text = text,link = link)
        send_mail(auth_user =settings.EMAIL_HOST_PASSWORD, subject=subject, message = "Plain text version of the email"
        ,html_message = htmlMessage, from_email = settings.EMAIL_HOST_USER, recipient_list = [user.email,])
        return  True        
    except Exception as e:
        print("=============="+str(e))
        return  False        
def activate_account(uidb64, token):  
    User = get_user_model()
    try:
        uid = str(urlsafe_base64_decode(uidb64), 'utf-8')
        user = User.objects.get(pk=uid)
    except (TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None
    if user is not None and default_token_generator.check_token(user, token):
        user.is_active = True
        user.save()
        return HttpResponse('Thank you for your email confirmation. Now you can login your account.')
    else:
        return HttpResponse('Activation link is invalid!')
