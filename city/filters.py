import django_filters
from .models import Employee
from .models import EmpSalary

class EmployeeFilter(django_filters.FilterSet):

    class Meta:
        model = Employee
        fields = '__all__'
