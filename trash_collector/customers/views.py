from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from .models import Customer
# Create your views here.

# TODO: Create a function for each path created in customers/urls.py. Each will need a template as well.


def index(request):
    # The following line will get the logged-in in user (if there is one) within any view function
    user = request.user
    try:
        # This line inside the 'try' will return the customer record of the logged-in user if one exists
        logged_in_customer = Customer.objects.get(user=user)
        context = {
            'logged_in_customer': logged_in_customer
        }
    except:
        return HttpResponseRedirect(reverse('customers:register'))

    return render(request, 'customers/index.html', context)


def create(request):
    """Create a new user with a name, address, zip code, and requested pickup day"""
    if request.method == 'POST':
        user = request.user
        name = request.POST.get('name')
        address = request.POST.get('address')
        zip_code = request.POST.get('zip_code')
        weekly_pickup_day = request.POST.get('weekly_pickup_day')
        new_customer = Customer(name=name, address=address, zip_code=zip_code, user=user,weekly_pickup_day=weekly_pickup_day)
        new_customer.save()
        return HttpResponseRedirect(reverse('customers:index'))
    else:
        return render(request, 'customers/register.html')

def account_details(request):
    if not request.user.groups.filter(name="Customers").exists():
        return render(request, 'home.html')
    user = request.user
    customer = Customer.objects.get(user=user)
    context = {'customer':customer}
    return render(request, 'customers/account_details.html', context)

def change_pickup_day(request):
    user = request.user
    customer = Customer.objects.get(user=user)
    if request.method == 'POST':
        change_weekly_pickup_day = request.POST.get('change_pickup_day')
        customer.weekly_pickup_day = change_weekly_pickup_day
        customer.save()
        return HttpResponseRedirect(reverse('customers:index'))
    else:
        context = {'customer':customer}
        return render(request, 'customers/change_pickup_day.html', context)