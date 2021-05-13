from django.contrib import admin
from .models import Employee, EmpSalary

# Register your models here.


class EmployeeFilter(admin.ModelAdmin):
    list_display = ['id', 'name', 'address', 'phone', 'designation']
    search_fields = ['name', 'address', 'designation', 'phone']
    list_filter = ['name', 'address', 'designation']


class EmpSalaryFilter(admin.ModelAdmin):
    list_display = ['id', 'salary', 'emp_id']
    search_fields = ['id', 'salary', 'emp_id']
    list_filter = ['id', 'salary', 'emp_id']


admin.site.register(Employee, EmployeeFilter)
admin.site.register(EmpSalary, EmpSalaryFilter)
