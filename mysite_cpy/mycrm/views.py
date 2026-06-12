#from django.shortcuts import render
#
#def index(request):
#    return render(request, 'core/index.html')
from django.shortcuts import render
from .models import Customer

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