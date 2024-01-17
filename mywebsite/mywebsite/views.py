from django.shortcuts import render
from django.http import HttpResponse
# from django.contrib.auth import User
from formapp2 import signup


def regis(request):
    if request.method == "POST":
        User = request.POST.get('username')
        Em = request.POST.get('email')
        psw1 = request.POST.get('pass1')
        psw2 = request.POST.get('pass2')
        User = signup(username=User,email=Em,password=psw1,password2=psw2)
        User.save()

        items = signup.objects.all()

    # Convert the data to a string format
        data_str = "\n".join([f"{item.serial_no}  - {item.created_at} - {item.username} - {item.email} - {item.password} - {item.password2}" for item in items])

    # Return the data in an HttpResponse
        return HttpResponse(data_str, content_type='text/plain')
    
    return render(request,"register.html")


# your_app_name/views.py
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages

def custom_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        psw = request.POST.get('psw')
        user = authenticate(request, username=username, password=psw)
        

        if user is not None:
            login(request, user)
            return HttpResponse("Login successfull")  # Replace 'home' with the URL name of your home page
        else:
            return HttpResponse("Login failed")
            

    return render(request, 'login.html')  # Specify the path to your login template


# Create your views here.
