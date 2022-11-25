from cmath import log
from tkinter import E
from django.shortcuts import redirect, render
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate , login , logout
from django.http import HttpResponseRedirect,HttpResponse
from .models import Profile
from django.contrib.auth import logout

# Login functionality

def login_page(request):
    if request.method == 'POST':
        # If the request method is POST, then 
        # extract input credentials-email and password
        email = request.POST.get('email')
        password = request.POST.get('password')

        # Find the user object with input email from User database
        user_obj = User.objects.filter(username = email)

        # If no such email exists, warning message is displayed
        if not user_obj.exists():
            messages.warning(request, 'Account not found.')
            return HttpResponseRedirect(request.path_info)

        # This was an "attempt" to incorporate email authentication
        # Checking whether user verified or not

        # if not user_obj[0].profile.is_email_verified:
        #     messages.warning(request, 'Your account is not verified.')
        #     return HttpResponseRedirect(request.path_info)

        # If email exists, Authenticating user
        user_obj = authenticate(username = email , password= password)
        # On successful authentication, login the user
        if user_obj:
            login(request , user_obj)
            return redirect('/')
        # Wrong password, Display warning
        messages.warning(request, 'Invalid credentials')
        return HttpResponseRedirect(request.path_info)

    return render(request ,'accounts/login.html')

# Register functionality
def register_page(request):

    # If the request method is POST, then 
    # extract input information of user
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        password = request.POST.get('password')

        # Find the user object with input email from User database
        user_obj = User.objects.filter(username = email)

        # If email already exists, we display warning
        if user_obj.exists():
            messages.warning(request, 'Email is already taken.')
            return HttpResponseRedirect(request.path_info)
        # Else we create and save a new user object with given information
        user_obj = User.objects.create(first_name = first_name , last_name= last_name , email = email , username = email)
        user_obj.set_password(password) #sets user password
        user_obj.save()
        messages.success(request, 'Successfully registered.')
        return HttpResponseRedirect(request.path_info)


    return render(request ,'accounts/register.html')

# Logout functionality
def logout_user(request):
    try:
        # If user was not login, then the below gives an error
        logout(request) # logout user
        return redirect('login')
    except:
        return redirect('login')


# This was an "attempt" to incorporate email authentication
# Activates user email

def activate_email(request , email_token):
    try:
        user = Profile.objects.get(email_token= email_token)
        user.is_email_verified = True
        user.save()
        return redirect('/')
    except Exception as e:
        return HttpResponse('Invalid Email token')




