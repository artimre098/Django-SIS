from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request,'home.html',{})

def acs(request):
    return render(request,'admin/admin-home.html',{})