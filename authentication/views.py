from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
# Create your views here.

def home(request):
    return render(request,"index.html")

def signup(request):

    if request.method == 'POST':
        # print(request.POST["username"])
        username = request.POST["username"]
        firstname = request.POST['firstname']
        lastname = request.POST["lastname"]
        email = request.POST["email"]
        password = request.POST["password"]
        cPass = request.POST["confirmpassword"]

        myUser = User.objects.create_user(username,email,password)

        myUser.first_name = firstname
        myUser.last_name = lastname

        myUser.save()

        messages.success(request,"Your account has been successfully created.")

        return redirect('signin')


    return render(request,"authentication/signup.html")

def signin(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username = username, password = password)

        if user is not None:
            form = login(request, user)
            messages.success(request, f' welcome {username} !!')
            return redirect('home')
        else:
            messages.info(request, f'account done not exit please sign in')
            return redirect('home')


    return render(request,"authentication/signin.html")
    
def signout(request):
    logout(request)
    messages.success(request,"logged out successfully!")
    return redirect('home')

