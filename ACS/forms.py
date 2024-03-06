from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import Record

class SignUpForm(UserCreationForm):
	email = forms.EmailField(label="", widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Email Address'}))
	first_name = forms.CharField(label="",max_length=100,widget=forms.TextInput(attrs={'class':'form-control','placeholder':'First Name'}))
	last_name = forms.CharField(label="",max_length=100,widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Last Name'}))

	class Meta:
		model = User
		fields = ('username','first_name','last_name','email','password1','password2')

	def __init__(self,*args,**kwargs):
		super(SignUpForm,self).__init__(*args,**kwargs)

		self.fields['username'].widget.attrs['class'] = 'form_control'
		self.fields['username'].widget.attrs['placeholder'] = 'User Name'
		self.fields['username'].label =''
		self.fields['username'].help_text = '<span class="form-text text-muted"><br/><small>Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only. </small></span>'

		self.fields['password1'].widget.attrs['class'] = 'form_control'
		self.fields['password1'].widget.attrs['placeholder'] = 'Password1'
		self.fields['password1'].label =''
		self.fields['password1'].help_text = '<ul class="form-text text-muted small"><li>Your password can\'t be too similar to your other personal information.</li><li>Your password must contain at least 8 characters.</li><li>Your password can\'t be a commonly used password.</li><li>You password can\'t be entirely numeric.</li></ul>'

		self.fields['password2'].widget.attrs['class'] = 'form_control'
		self.fields['password2'].widget.attrs['placeholder'] = 'Password2'
		self.fields['password2'].label =''
		self.fields['password2'].help_text = '<span class="form-text text-muted"><br/><small>Enter the same password above </small></span>'


#add Record form
class AddRecordForm(forms.ModelForm):
	YEAR_CHOICES = [
        ('1st', '1st Year'),
        ('2nd', '2nd Year'),
        ('3rd', '3rd Year'),
        ('4th', '4th Year'),
    ]
	 
	student_id =  forms.CharField(required=True,label="",max_length=100,widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Student ID'}))
	first_name =  forms.CharField(required=True,label="",max_length=100,widget=forms.TextInput(attrs={'class':'form-control','placeholder':'First Name'}))
	last_name = forms.CharField(required=True,label="",max_length=100,widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Last Name'}))
	year_level = forms.ChoiceField(choices=YEAR_CHOICES, required=True, label="", widget=forms.Select(attrs={'class': 'form-control', 'placeholder': 'Year Level'}))
	email = forms.CharField(required=True,label="",max_length=100,widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Email Address'}))
	
	class Meta:
		model = Record
		exclude = ("user",)

	def save(self, commit=True):
        # Save the Record instance
		record = super(AddRecordForm, self).save(commit=False)
        
        # Create a new user with first_name and last_name as username and password
		user = User.objects.create_user(username=self.cleaned_data['first_name'],password=self.cleaned_data['last_name'])
        
        # Link the new user to the Record instance
		record.user = user

		if commit:
			record.save()

		return record