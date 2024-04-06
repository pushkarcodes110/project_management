from django.contrib.auth import authenticate, login as auth_login
from django.shortcuts import render, redirect
from django.contrib import messages  # Import messages module for displaying error messages
from .models import User

def login(request):
    if request.method == 'POST':
        email = request.POST.get('email', '')
        password = request.POST.get('password', '')

        if email and password:
            user = authenticate(request, email=email, password=password)

            if user is not None:
                auth_login(request, user)
                return redirect('/')
            else:
                # Display an error message if authentication fails
                messages.error(request, 'Invalid email or password. Please try again.')

    return render(request, 'account/login.html')

from django.contrib.auth.models import User
from django.shortcuts import render, redirect

def signup(request):
    if request.method == 'POST':
        name = request.POST.get('name', '')
        email = request.POST.get('email', '')
        password1 = request.POST.get('password1', '')
        password2 = request.POST.get('password2', '')

        if name and email and password1 and password2:
            if password1 == password2:
                user = User.objects.create_user(username=name, email=email, password=password1)
                print('User created:', user)
                return redirect('/login/')
            else:
                print('Passwords do not match')
        else:
            print('Please fill in all the required fields')

    return render(request, 'account/signup.html')