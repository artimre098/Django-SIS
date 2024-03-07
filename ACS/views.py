from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import SignUpForm, AddRecordForm
from .models import Record

# Create your views here.

def home(request):
    return render(request,'home.html',{})

def acs(request):
    	#Check to see if logging in
	records = Record.objects.all()

	if request.method == 'POST':
		username = request.POST['username']
		password = request.POST['password']

		#authenticate
		user = authenticate(request, username=username,password=password)
		if user is not None:
			login(request,user)
			messages.success(request,"You have been logged In!")
			return redirect('acs')
		else:
			messages.success(request,"There was an error Logging in, Please try again...")
			return redirect('acs')
	else:
		return render(request,'admin/admin-home.html',{})

def logout_user(request):
	logout(request)
	messages.success(request,"You have been Logged Out...")
	return redirect('acs')
	

def register(request):
    if request.method == 'POST':
        form = AddRecordForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['student_id']
            password = form.cleaned_data['student_id']
            user = authenticate(username=username,password=password)
            messages.success(request,"Student successfully registered")
            return redirect('acs')
            
    else:
        form = AddRecordForm()
        return render(request, 'admin/register.html',{'form':form})