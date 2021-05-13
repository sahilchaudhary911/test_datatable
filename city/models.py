from django.db import models

# Create your models here.


class Employee(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=512, null=True)
    address = models.CharField(max_length=512, null=True)
    phone = models.FloatField(null=True)
    designation = models.CharField(max_length=512, null=True)

    def __str__(self):
        return self.name


class EmpSalary(models.Model):
    id = models.AutoField(primary_key=True)
    salary = models.FloatField(null=True, blank=True)
    emp_id = models.ForeignKey(Employee, on_delete=models.CASCADE)

