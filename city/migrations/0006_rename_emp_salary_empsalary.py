# Generated by Django 3.2 on 2021-04-29 14:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('city', '0005_auto_20210429_1320'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='emp_salary',
            new_name='EmpSalary',
        ),
    ]