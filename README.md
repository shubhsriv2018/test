python3 -m venv venv -> create virtual env
source venv/bin/activate -> activate virtual env
pip install Django -> PIP is used to install python framworks and packages.. this command is to install Django
python -m Django --version -> to check Django version
django-admin startproject <project_name> -> to start a new project in Django
python manage.py migrate -> to setup/initialize the database, i.e. sqllite
python manage.py runserver 0.0.0.0:8000 -> command to start the application frontend/local web server

CRM TOOL - Client Relationship management tool
basic of sql commands ---> 


python manage.py startapp mycrm -> initialize a new application
go to default app settings.py and register your app

ex: 
INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "mycrm",
]

go to default app urls.py and direct the default url to your app 

ex: 
from django.contrib import admin
from django.urls import path
from mycrm.views import index

urlpatterns = [
    path("admin/", admin.site.urls),
    path('', index, name='index'),
]

create a template for you app frontend
-> create a folder 'Templates' inside your app
-> inside templates create another folder for easy management (ex: mycrm)
-> create the index.html

ex: 

{% block content %}
<h1>CRM Tool</h1>
<p>Welcome to our CRM tool<p>
{% endblock %}

create the views.py file (views.py is the first file that is called upon app launch)
 -> inside this we need to call the index.html
 ex:

from django.shortcuts import render

def index(request):
    return render(request, 'mycrm/index.html')

now register the default url to trigger index.html
 -> go to the default app 'mysite'
 -> edit urls.py
ex:

from django.contrib import admin
from django.urls import path
from mycrm.views import index

urlpatterns = [
    path("admin/", admin.site.urls),
    path('', index, name='index'),
]

Authentication setup for app and Login Page Creation

--> mysite>mycrm>views.py

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
    return render(request, 'mycrm/index.html')

--> Create templates/mycrm/login.html

<!DOCTYPE html>
<html>
<head>
	<title> CRM Tool Login</title>
</head>
<body>

    <h2>CRM Login</h2>

    {% if messages %}
        {% for message in messages %}
            <p style="color:red">{{message}}</p>
        {% endfor %}
    {% endif %}

    <form method="post">
        {% csrf_token %}

        <p>
            Username:
            <input type="text" name="username">
        </p>

        <p>
            Password:
            <input type="password" name="password">
        </p>
 
        <button type="submit">Login</button>
    </form>

</body>
</html>

--> In the default app add the login url

mysite/mysite/urls.py

urlpatterns = [
    path("admin/", admin.site.urls),
    path('', index, name='index'),
    path('login/', login_view, name='login'),
]

mysite/mysite/settings.py

LOGIN_URL = '/login/'

--> Create a superuser (admin:admin123) 

python manage.py createsuperuser

--> Verify user exists

python manage.py shell
from django.contrib.auth.models import User

User.objects.all()

=======
--> update models.py

from django.db import models

# Create your models here.
class Customer(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(blank=True)
    phone = models.CharField(max_length=20, blank=True)

    def __str__(self):
        return self.name

--> run below command to create the db tables:
python manage.py makemigrations mycrm - get the db ready for migration
python manage.py migrate - migrate the models in db

--> update views.py

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

--> update urls.py to direct the default to login page

"""
URL configuration for mysite project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path
from mycrm.views import index
from mycrm.views import login_view

urlpatterns = [
    path("admin/", admin.site.urls),
    path("index/", index, name='index'),
    path('', login_view, name='login'),
]


--> add some test data to the customer table

from mycrm.models import Customer

Customer.objects.create(
    name="ABC Corp",
    email="abc@test.com",
    phone="9999999999"
)

Customer.objects.create(
    name="XYZ Ltd",
    email="xyz@test.com",
    phone="8888888888"
)

--> update mycrm/base.html as below

<!DOCTYPE html>
<html>
<head>
	<title> CRM </title>
</head>
<body>

<nav>
	<a href="/">Home</a> |

</nav>

{% block content %}
{% endblock %}

</body>
</html>

--> update mycrm/login.html as below

<!DOCTYPE html>
<html>
<head>
	<title> CRM Tool Login</title>
</head>
<body>

    <h2>CRM Login</h2>

    {% if messages %}
        {% for message in messages %}
            <p style="color:red">{{message}}</p>
        {% endfor %}
    {% endif %}

    <form method="post">
        {% csrf_token %}

        <p>
            Username:
            <input type="text" name="username">
        </p>

        <p>
            Password:
            <input type="password" name="password">
        </p>
 
        <button type="submit">Login</button>
    </form>

</body>
</html>

--> update the index.html to show the table details

{% extends 'mycrm/base.html' %}

{% block content %}
<h1>CRM Tool</h1>
<p>Welcome to our CRM tool<p>

    <h2>Customer Dashboard</h2>

    <table border=""1" cleepadding="10">
        <tr>
            <th>ID</th>
            <th>Name</th>
            <th>Email</th>
            <th>Phone</th>
        </tr>
        {% for customer in customers %}
        <tr>
            <td>{{customer.id}}</td>
            <td>{{customer.name}}</td>
            <td>{{customer.email}}</td>
            <td>{{customer.phone}}</td>
        </tr>
        {% endfor %}
    </table>
{% endblock %}




