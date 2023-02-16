from django.contrib import auth
from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from auth_app.forms import CustomUser
from django.contrib.auth import authenticate, login, logout

# Create your views here.
def login(request):
    if request.method=='GET':
        return render(request, 'login.html')
    else:
        username = request.POST['user_email']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('home')

        else:
            messages.info(request, 'Invalid Email or Password')
            return render(request, 'login.html')

def signup(request):
    user = CustomUser()
    if request.method=='GET':
        return render(request, 'signup.html', {'user':user})
    # if request.method=='GET':
    #     return render(request, 'signup.html', {'user':User})
    # else:
    #     username = request.POST['username']
    #     email = request.POST['email']
    #     password = request.POST['password']
    #     phone = request.POST['phone']

    #     user.objects.create_user(full_name=username, email=email, password=password, phone_number=phone)

    #     return redirect('login')

def logout_view(request):
    logout(request)
    return redirect('login')