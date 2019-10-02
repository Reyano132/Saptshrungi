from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from client.models import Client
from service.models import Service
from task.models import Task
from user.models import User

class DateInput(forms.DateInput):
	input_type='date'

class WorkerRegisterForm(UserCreationForm):
	birthdate=forms.DateField(widget=DateInput)
	class Meta:
		model=get_user_model()
		widget={'birthdate':DateInput()}
		fields = ['username', 'password1', 'password2','email','first_name','last_name','phone_number','birthdate']

class ClientRegisterForm(forms.ModelForm):
	birthdate=forms.DateField(widget=DateInput)
	class Meta:
		model=Client
		widget={'birthdate':DateInput()}
		fields='__all__'

class AddServiceForm(forms.ModelForm):
	class Meta:
		model=Service
		fields = '__all__'

class CreateTaskForm(forms.ModelForm):
	priority=forms.ChoiceField(choices=[(x,x) for x in ['Very low','Low', 'Medium', 'High','Very high']])
	class Meta:
		model=Task 
		fields = ['for_client','assigned_to','service','description','priority','charges']		
			
	def __init__(self, *args, **kwargs):
		super(CreateTaskForm, self).__init__(*args, **kwargs)
		if self.instance:
			self.fields['assigned_to'].queryset = User.objects.filter(is_superuser = False)

class AssignTaskForm(forms.ModelForm):
	priority=forms.ChoiceField(choices=[(x,x) for x in ['Very low','Low', 'Medium', 'High','Very high']])
	due_date=forms.DateField(widget=DateInput)
	class Meta:
		model=Task 
		widget={'due_date':DateInput()}
		fields = ['for_client','assigned_to','service','description','priority','charges','due_date']		
			
	def __init__(self, *args, **kwargs):
		super(AssignTaskForm, self).__init__(*args, **kwargs)
		if self.instance:
			self.fields['assigned_to'].queryset = User.objects.filter(is_superuser = False)

