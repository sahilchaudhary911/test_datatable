from django.shortcuts import render
from django.http import HttpResponse
from .models import EmpSalary
from .filters import EmployeeFilter
from .models import Employee
from django.views.generic import TemplateView

# Create your views here.


def homepage(request):
    data = EmpSalary.objects.all()
    # f = EmployeeFilter(request.GET, queryset=Employee.objects.all())
    f = []
    employees = Employee.objects.all()
    for emp in employees:
        # salary = EmpSalary.objects.filter(emp_id=emp.id).values_list('salary', flat=True)[0]
        salary = EmpSalary.objects.filter(emp_id=emp.id).values()[0]['salary']
        d = emp.__dict__
        d['salary'] = salary
        f.append(d)
    return render(request, 'index.html', {'data': data, 'filter': f})


def others(request):
    data = EmpSalary.objects.all()
    return render(request, 'others.html', {'data': data})
