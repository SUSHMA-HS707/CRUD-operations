from django.shortcuts import render,redirect
from FbvApp.models import Employee
from FbvApp.forms import EmployeeForm
# Create your views here.
def display(request):
    e=Employee.objects.all()
    d={'emp':e}
    return render(request,'FbvApp/index.html',d)
def insert_view(request):
    f=EmployeeForm()
    if request.method=="POST":
        f=EmployeeForm(request.POST)
        if f.is_valid():
            f.save(commit=True)
        return redirect("/")
    d={'form':f}
    return render(request,'FbvApp/insert.html',d)
def delete_view(request,id):
    e=Employee.objects.get(id=id)
    e.delete()
    return redirect('/')
def update_view(request,id):
    e=Employee.objects.get(id=id)
    if request.method=='POST':
        f=EmployeeForm(request.POST,instance=e)
        if f.is_valid():
            f.save(commit=True)
        return redirect("/")
    d={'emp':e}
    return render(request,'FbvApp/update.html',d)
