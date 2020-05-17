from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Employee
from .forms import Employeeform




def list(request):
    employee = {'employees' : Employee.objects.all()}
    return render(request, 'list.html', employee)

def home(request):
    if request.method == "GET":
        employee = Employeeform()
        return render(request, 'form.html', {'employees': employee})
    else:
        employee = Employeeform(request.POST)
        if employee.is_valid():
            employee.save()
        return redirect('/b/a')

def employee_delete(request, id=0): 
    employee = Employee.objects.get(pk=id)
    employee.delete()
    return redirect('/b/a')    

def employee_list(request, id=0):
    if request.method == "GET":
        if id==0:
            employee = Employeeform()
        else:
            data = Employee.objects.get(pk=id)
            employee = Employeeform(instance=data)
        return render(request, 'form.html', {'employees': employee})
    else:  
        if id==0:
            employee = Employeeorm(request.POST)
        else:
            data=Employee.objects.get(pk=id)
            employee=EmployeeForm(request.POST, instance=data)
        if  employee.is_valid():
            employee.save()
        return redirect('/b/a')

       
        


# Create your views here.
