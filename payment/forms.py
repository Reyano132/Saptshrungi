from django import forms
from .models import PaymentData


class DateInput(forms.DateInput):
	input_type='date'


class CreatePaymentForm(forms.ModelForm):
	dated=forms.DateField(widget=DateInput)
	payment_method=forms.ChoiceField(choices=[(x,x) for x in ['Debit Card','Credit Card', 'Cash', 'Online Payment']])
	class Meta:
		model=PaymentData
		widget={'dated':DateInput()}	
		fields=['for_client','for_task','dated','value','payment_method','card_number']

	def __init__(self, *args, **kwargs):
		super(CreatePaymentForm, self).__init__(*args, **kwargs)