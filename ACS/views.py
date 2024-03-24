from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.views.decorators.http import require_http_methods
from django.contrib import messages
from .forms import SignUpForm, AddRecordForm, UpdateRecordForm, AccountPayableForm
from .models import Record, AccountPayable, Payment
from django.contrib.auth.models import User

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
            # If form is invalid, render the form template again with the errors
            return render(request, 'admin/register.html', {'form': form})
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
		accounts = AccountPayable.objects.all()
		payments = Payment.objects.all()
		return render(request,'admin/student-record.html',{'record':record,'accounts':accounts,'payments':payments})
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
	delete_user = User.objects.get(username=pk)
	if request.user.is_authenticated:
		delete_it.delete()
		delete_user.delete()
		messages.success(request,"Employee Records has been deleted")
		return redirect('acs')
	else:
		messages.success(request,"You Must be Logged In to View That Page")
		return redirect('acs')
	

def add_account(request):
    if request.method == 'POST':
        form = AccountPayableForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,"Account successfully added")
            return redirect('acs')
        else:
            # If form is invalid, render the form template again with the errors
            return render(request, 'admin/add-account.html', {'form': form})
    else:
        form = AccountPayableForm()
        return render(request, 'admin/add-account.html',{'form':form})

@require_http_methods(["GET", "POST"])
def pay_account(request, student_id, account_id):
	if request.user.is_authenticated:
		if request.method == 'POST':
			amount_tendered = request.POST.get('amount_tendered')
			payment_date = request.POST.get('payment_date')
			try:
				# Retrieve record and account objects
				record = Record.objects.get(student_id=student_id)
				account = AccountPayable.objects.get(id=account_id)
				

				# Create a new Payment instance
				payment = Payment.objects.create(
					student=record,
					payable=account,
					amount_paid=amount_tendered,
					receiver_user_id=request.user.username,  # Assuming you want to save the username of the logged-in user
					payment_date=payment_date
				)
				
				# Optionally, you can save the payment date from the request or use the current date
				
				messages.success(request, "Payment details saved successfully.")
				return redirect('acs')
			
			except (Record.DoesNotExist, AccountPayable.DoesNotExist):
				messages.error(request, "Record or account not found.")
				return redirect('acs')
			
		
	else:
		messages.error(request, "You must be logged in to view that page.")
		return redirect('acs')