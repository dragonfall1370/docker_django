# from linear.account.decorator import unauthenticated_user
from django.contrib import auth
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponse
from .forms import CreateUserForm
from django.contrib import messages
from django.contrib.auth.models import User

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .decorator import unauthenticated_user

# Create your views here.
@login_required(login_url='login')
def hompage(request):
    return render(request, 'account/homepage.html')


def hompage_without_login(request):
    return render(request, 'account/homepage_without_login.html')

@login_required(login_url='login')
def users(request):
    return render(request, 'account/normal-user.html')

@login_required(login_url='login')
def about(request):    
    return render(request, 'account/about.html')

@unauthenticated_user
def loginpage(request):     
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username = username, password = password)

        if user is not None:
            login(request, user)
            return redirect('homepage')
        else:
            messages.info(request, 'Username OR password is in correct')
            return render(request, 'account/login.html')
    return render(request, 'account/login.html')

@login_required(login_url='login')
def logoutUser(request):
    logout(request)
    return redirect ('login')

@unauthenticated_user
def registerpage(request):

    form = CreateUserForm()

    if request.method == "POST":
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request, "Account was created for " + user)
            return redirect("login")
    return render(request, 'account/register.html',{
        'form':form
    })

