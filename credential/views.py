from django.contrib import messages
from django.contrib.auth.models import User,auth
from django.shortcuts import render, redirect


# Create your views here.


def register(request):
    if request.method=='POST':

       username = request.POST['username']
       firstname = request.POST['firstname']
       lastname = request.POST['lastname']
       email = request.POST['email']
       password = request.POST['password']
       cpassword = request.POST['confirm password']
       if password==cpassword:
        user = User.objects.create_user(username=username, password=password, firstname=firstname, lastname=lastname,
                                    email=email, confirmpassword=cpassword)
       user.seve();
       print('user created')
    else:
        print('user dismatch')
    return render(request,'register.html')


def login(request):
    return render(request,'login.html')


def logout(request):
    auth.logout(request)
    return redirect('/')