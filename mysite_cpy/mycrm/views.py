#from django.shortcuts import render
#
#def index(request):
#    return render(request, 'core/index.html')
#from django.shortcuts import render
from .models import Customer
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(
            request,
            username=username,
            password=password
        )

        if user is not None:
            login(request, user)
            return redirect('index')
        else:
            messages.error(request, 'Invalid username or password')

    return render(request, 'mycrm/login.html')

@login_required   
def index(request):
    customers = Customer.objects.all()

    return render(
        request,
        'mycrm/index.html',
        {
            'customers': customers
        }
    )
#def about(request):
#    return render(request, 'core/about.html')