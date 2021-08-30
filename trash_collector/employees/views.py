from django.http import HttpResponse
from django.http.response import HttpResponseRedirect
from django.shortcuts import render
from django.apps import apps
from django.urls import reverse
from .models import Employee
from datetime import date

# Create your views here.

# TODO: Create a function for each path created in employees/urls.py. Each will need a template as well.


def index(request):
    # This line will get the Customer model from the other app, it can now be used to query the db for Customers
    Customer = apps.get_model('customers.Customer')
    all_customers = Customer.objects.all()
    user = request.user
    try:
        logged_in_employee = Employee.objects.get(user = user)

    except:
        return HttpResponseRedirect(reverse('employees:create'))

    context = {'logged_in_employee':logged_in_employee,
            'all_customers':all_customers
        }
    return render(request, 'employees/index.html', context)



def create(request):
    if request.method == 'POST':
        user = request.user
        name = request.POST.get('name')
        zip_code = request.POST.get('zip_code')
        new_employee = Employee(name = name, user = user, zip_code = zip_code)
        new_employee.save()
        return HttpResponseRedirect(reverse('employees:index'))
    else:
        return render(request, 'employees/create.html')

def daily_view(request):
    user = request.user
    logged_in_employee = Employee.objects.get(user=user)
    Customers = apps.get_model('customers.Customer')
    all_customers = Customers.objects.all()
    current_date = date.today()
    weekday = current_date.strftime('%A')
    my_customers = []
    for customer in all_customers:
            if customer.zip_code == logged_in_employee.zip_code and (customer.weekly_pickup_day == weekday or customer.one_time_pickup == weekday):
                my_customers.append(customer)
    context = { 'my_customers' : my_customers,
                'weekday': weekday}
    return render(request, 'employees/daily_view.html', context)
