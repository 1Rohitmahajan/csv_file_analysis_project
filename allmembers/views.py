from django.shortcuts import render,redirect
from django.contrib.auth import authenticate , login, logout
from django.contrib import messages
from django.contrib.auth.models import User

def login_user(request):
    if request.method=="POST":
        username=request.POST['username']
        password=request.POST['password']
        user=authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            messages.success(request, "Successfully Logged In")
            return redirect('index')
        else:
            messages.info(request, 'invalid credentials')
            return render(request, 'authenticate/login.html')

    else:
        return render(request,'authenticate/login.html',{})
    
def logoutuser(request):
    logout(request)
    messages.success(request, 'Logout successfully')
    return redirect('/')

