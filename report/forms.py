from django import forms
from .models import ReportData


class DateInput(forms.DateInput):
	input_type='date'


class GenerateReportForm(forms.ModelForm):
	class Meta:
		model=ReportData

	def __init__(self, *args, **kwargs):
		super(GenerateReportForm, self).__init__(*args, **kwargs)