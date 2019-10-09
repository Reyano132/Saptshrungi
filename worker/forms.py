from django import forms
from user.models import User
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm


class DateInput(forms.DateInput):
	input_type='date'

class WorkerRegisterForm(UserCreationForm):
	birthdate=forms.DateField(widget=DateInput)
	class Meta:
		model=get_user_model()
		widget={'birthdate':DateInput()}
		fields = ['username', 'password1', 'password2','email','first_name','last_name','phone_number','birthdate']
