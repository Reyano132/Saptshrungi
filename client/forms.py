from django import forms
from .models import Client

class DateInput(forms.DateInput):
	input_type='date'

class ClientRegisterForm(forms.ModelForm):
	birthdate=forms.DateField(widget=DateInput)
	class Meta:
		model=Client
		widget={'birthdate':DateInput()}
		fields='__all__'