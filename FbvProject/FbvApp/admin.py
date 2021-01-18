from django.contrib import admin
from FbvApp.models import Employee

# Register your models here.
class EmployeeAdmin(admin.ModelAdmin):
    l=['eno','ename','esal','eaddr']
admin.site.register(Employee,EmployeeAdmin)
