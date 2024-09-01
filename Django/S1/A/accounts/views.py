from django.shortcuts import render , redirect
from .forms import UserRegistrationForm , UserLoginForm
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate , login , logout

def user_register(request):

    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            User.objects.create_user(username=cd['register_form_username'] , password=cd['register_form_password'] , email=cd['register_form_email'])
            messages.add_message(request , messages.SUCCESS , 'successfully registered' , 'success')
            return redirect('home')
    else:
        form = UserRegistrationForm()
        return render(request , 'account_app/register.html' , context={'form' : form})




def user_login(request):
    if request.method =='POST':
        form = UserLoginForm(request.POST) # with the data coming from POST
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(request , username=cd['login_form_username'] , password=cd['login_form_password'])
            if user is not None:
                login(request , user)
                messages.success(request , 'loggined successfully' , 'success')
            else:
                messages.error(request , 'invalid credentials' , 'danger')

    else:#if request was get :
        form = UserLoginForm()
    return  render(request , 'account_app/login.html' , context={'form' : form})

def user_logout(request):
    logout(request)
    messages.success(request , 'loggout successfully' , 'success')
    return redirect('home')
