
from django.contrib.auth import authenticate, login as auth_login, get_user_model
from django.shortcuts import render, redirect
from django.contrib import messages

def login(request):
    if request.method == 'POST':
        email = request.POST.get('email', '')
        password = request.POST.get('password', '')

        if email and password:
            
                user = authenticate(request, username=email, password=password)
                print('user:', user)
                if user is not None:
                    
                    auth_login(request, user)
                    print('Logged in user:', request.user.email)
                    print('Is authenticated?', request.user.is_authenticated)
                    return redirect('/')
                else:
                    messages.error(request, 'Invalid email or password.')

    return render(request, 'account/login.html')

def signup(request):
    if request.method == 'POST':
        name = request.POST.get('name', '')
        email = request.POST.get('email', '')
        password1 = request.POST.get('password1', '')
        password2 = request.POST.get('password2', '')

        if name and email and password1 and password2:
            if password1 == password2:
                User = get_user_model()
                # Create user with create_user method from get_user_model()
                user = User.objects.create_user(name=name, email=email, password=password1)
                print('User created:', user)
                return redirect('/login/')
            else:
                print('Passwords do not match')
        else:
            print('Please fill in all the required fields')

    return render(request, 'account/signup.html')