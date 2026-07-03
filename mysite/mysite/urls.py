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
from mycrm.views import add_customer
from mycrm.views import delete_customer
from mycrm.views import customers
from mycrm.views import leads

urlpatterns = [
    path("admin/", admin.site.urls),
    path("index/", index, name='index'),
    path('', login_view, name='login'),
    path('customers/', customers, name='customers'),
    path('leads/', leads, name='leads'),
    path('customer/add/', add_customer, name='add_customer'),
    path('customer/delete/<int:customer_id>/', delete_customer, name='delete_customer'),
]
