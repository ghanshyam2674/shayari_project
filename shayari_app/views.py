from django.shortcuts import render, redirect
from .forms import SignUpForm
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm, SetPasswordForm
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib.auth.decorators import login_required


# Create your views here.

# @login_required(login_url='login')
def index(request):
    return render (request, 'index.html')

def sign_up_user(request):
    if request.method == "POST":
        fm = SignUpForm(request.POST)
        if fm.is_valid():
            fm.save()
            messages.success(request, 'your account successfully created')
            return redirect ('login')
    else: fm = SignUpForm()
    return render (request, 'sign_up.html', {'form': fm})

def login_user(request):
    if not request.user.is_authenticated:
        if request.method == "POST":
            fm = AuthenticationForm(request=request, data=request.POST)
            if fm.is_valid():
                username = fm.cleaned_data['username']
                password = fm.cleaned_data['password']
                user = authenticate(username=username, password=password)
                if user is not None:
                    login(request, user)
                    return redirect ('index')
        else:  
            fm = AuthenticationForm()
    else:
        return redirect('index')        
    return render (request, 'login.html', {'form': fm})    

def logout_user(request):
    logout(request)
    return render (request, 'logout.html')

@login_required(login_url='login')
def password_change(request):
    if request.method == "POST": 
        fm = PasswordChangeForm(user=request.user, data=request.POST)
        if fm.is_valid():
            fm.save()
            update_session_auth_hash(request, fm.user)
            return redirect('index')
    else:
        fm = PasswordChangeForm(user=request.user)
    return render (request, 'password_change.html', {'form': fm})   


@login_required(login_url='login')
def reset_password(request):
    if request.method == "POST": 
        fm = SetPasswordForm(user=request.user, data=request.POST)
        if fm.is_valid():
            fm.save()
            update_session_auth_hash(request, fm.user)
            return redirect('index')
    else:
        fm = SetPasswordForm(user=request.user)
    return render (request, 'reset_password.html', {'form': fm})

