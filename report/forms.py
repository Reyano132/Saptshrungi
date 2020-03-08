from django import forms
from .models import ReportData


class DateInput(forms.DateInput):
	input_type='date'


class GenerateReportForm(forms.ModelForm):
	from_date=forms.DateField(widget=DateInput)
	to_date=forms.DateField(widget=DateInput)
	class Meta:
		model=ReportData
		fields=['from_date','to_date','client_name','employee_name']

	def __init__(self, *args, **kwargs):
		super(GenerateReportForm, self).__init__(*args, **kwargs)