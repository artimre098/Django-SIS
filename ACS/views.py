from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import SignUpForm, AddRecordForm, UpdateRecordForm
from .models import Record

# Create your views here.

def home(request):
    return render(request,'home.html',{})

def resume(request):
    return render(request,'my-resume.html',{})

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
		return render(request,'admin/admin-home.html',{'records':records})

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

def update_record(request,pk):
	if request.user.is_authenticated:
		current_record = Record.objects.get(student_id=pk)
		form = UpdateRecordForm(request.POST or None , instance=current_record)
		if form.is_valid():
			form.save()
			messages.success(request,"Students Records has been Updated")
			return redirect('acs')
		return render(request, 'admin/student-update.html',{'form':form})
	else:
		messages.success(request,"You Must be Logged In to View That Page")
		return redirect('acs')
	
def student_record(request,pk):
	if request.user.is_authenticated:
		record = Record.objects.get(student_id=pk)
		return render(request,'admin/student-record.html',{'record':record})
	else:
		messages.success(request,"You must be logged in to view that page")
		return redirect('acs')
	
# def update_record(request,pk):
# 	if request.user.is_authenticated:
# 		record = Record.objects.get(student_id=pk)
# 		return render(request,'admin/student-update.html',{'record':record})
# 	else:
# 		messages.success(request,"You must be logged in to view that page")
# 		return redirect('acs')
	
def delete_record(request,pk):
	delete_it = Record.objects.get(student_id=pk)
	
	if request.user.is_authenticated:
		delete_it.delete()
		messages.success(request,"Employee Records has been deleted")
		return redirect('acs')
	else:
		messages.success(request,"You Must be Logged In to View That Page")
		return redirect('acs')