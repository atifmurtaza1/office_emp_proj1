from django.http import HttpResponse
from django.shortcuts import render
from .models import *
from django.db.models import Q


# Create your views here.
def index(request):
    return render(request, 'index.html')


def all_emp(request):
    emps = Employee.objects.all()
    context = {
        'emps': emps
    }
    print(context)
    return render(request, 'view_all_emp.html', context)


def add_emp(request):
    if request.method == 'POST':  # Corrected syntax: replaced ';' with ':'
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        salary = request.POST['salary']   # Corrected spelling of 'salary'
        bonus =  request.POST['bonus']
        phone =  request.POST['phone']
        dept = request.POST['dept']
        role = request.POST['role']
        new_emp = Employee(first_name=first_name, last_name=last_name, salary=salary, bonus=bonus, phone=phone,
                           dept_id=dept, role_id=role)
        new_emp.save()
        return HttpResponse('Employee added successfully')  # Corrected spelling of 'successfully'
    elif request.method == 'GET':  # Corrected syntax: replaced ';' with ':'
        return render(request, 'add_emp.html')
    else:
        return HttpResponse('An Exception Occurred!')  # Corrected spelling of 'Exception'


def remove_emp(request, emp_id = 0):
    if emp_id:
        try:
            emp_to_be_removed = Employee.objects.get(id=emp_id)
            emp_to_be_removed.delete()
            return HttpResponse('Employee Removed Successfully')
        except:
            return HttpResponse('Please Enter a valid id')
    emps = Employee.objects.all()
    context = {
        'emps': emps
    }
    return render(request, 'remove_emp.html',context)


def filter_emp(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        dept = request.POST.get('dept')
        role = request.POST.get('role')
        emps = Employee.objects.all()

        # Construct filter query with OR conditions using Q objects
        if name:
            emps = emps.filter(Q(first_name__icontains=name) | Q(last_name__icontains=name))
        if dept:
            emps = emps.filter(dept__name__icontains =dept)
        if role:
            emps = emps.filter(role__name__icontains=role)

        context = {
            'emps': emps
        }
        return render(request, 'view_all_emp.html', context)

    elif request.method == 'GET':
        return render(request, 'filter_emp.html')

    else:
        return HttpResponse('Please Enter a correct detail')