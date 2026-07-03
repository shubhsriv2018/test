from .models import Customer
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages
from .forms import CustomerForm
from django.shortcuts import get_object_or_404

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

from .models import Customer
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages
from .forms import CustomerForm
from django.shortcuts import get_object_or_404

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

def add_customer(request):
    if request.method == "POST":
        form = CustomerForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = CustomerForm()

        return render(
            request,
            "mycrm/add_customer.html",
            {"form": form}
        )

def delete_customer(request, customer_id):
    customer = get_object_or_404(Customer, id=customer_id)
    customer.delete()
    return redirect('index')

def customers(request):
    customers = Customer.objects.all()

    return render(
        request,
        'mycrm/customers.html',
        {
            'customers' : customers
        }
    )

def leads(request):
    total_customers = Customer.objects.count()

    return render(
        request,
        'mycrm/leads.html',
        {
            'total_customers' : total_customers
        }
    )
