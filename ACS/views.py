from django.shortcuts import render
from .forms import AddRecordForm

# Create your views here.

def home(request):
    return render(request,'home.html',{})

def acs(request):
    return render(request,'admin/admin-home.html',{})

def register(request):
    if request.method == 'POST':
        form = AddRecordForm(request.POST)
        if form.is_valid():
            form.save()
            



    return render(request,'admin/register.html',{})