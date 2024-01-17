from django.shortcuts import render , redirect
from django.http import HttpResponse
# from django.contrib.auth import User
from .models import signup


def newuser(request):
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

from django.contrib.auth import authenticate, login
from django.contrib import messages



def custom_login(request):
      if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        try:
            user = signup.objects.get(username=username)
        except signup.DoesNotExist:
            # Handle case where the user does not exist
            return render(request, 'login.html', {'error_message': 'Invalid credentials'})

        # Check if the provided password matches the stored password hash
        if user.check_password(password):
            # If login is successful, you can access user data and then redirect
            # For example, you can pass user data to the next page using the session
            request.session['user_id'] = user.id
            request.session['username'] = user.username

            # Redirect to the next page (replace 'next_page' with the desired URL)
            return redirect('next_page')
        else:
            # Handle unsuccessful login (e.g., display an error message)
            return render(request, 'login.html', {'error_message': 'Invalid credentials'})

      return render(request, 'login.html')