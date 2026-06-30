from .models import Customer
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        print("Username:", username)
        print("Password:", password)

        user = authenticate(
            request,
            username=username,
            password=password
        )

        print("Authenticated User:", user)

        if user is not None:
            login(request, user)
            print("LOGIN SUCCESS")
            return redirect('index')
        else:
            print("LOGIN FAILED")
            messages.error(request, 'Invalid username or password')

    return render(request, 'mycrm/login.html')

@login_required
def index(request):
    customers = Customer.objects.all()
    
    return render(
    request, 
    'mycrm/index.html', 
    { 
        'customers' : customers 
    }
)
