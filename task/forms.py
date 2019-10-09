from django import forms
from .models import Task
from .models import User

class DateInput(forms.DateInput):
	input_type='date'

class CreateTaskForm(forms.ModelForm):
	priority=forms.ChoiceField(choices=[(x,x) for x in ['Very low','Low', 'Medium', 'High','Immediate']])
	due_date=forms.DateField(widget=DateInput)
	class Meta:
		model=Task 
		widget={'due_date':DateInput()}
		fields = ['for_client','assigned_to','service','description','priority','charges','due_date']		
			
	def __init__(self, *args, **kwargs):
		super(CreateTaskForm, self).__init__(*args, **kwargs)
		if self.instance:
			self.fields['assigned_to'].queryset = User.objects.filter(is_superuser = False)

class UpdateProgress(forms.ModelForm):
	class Meta:
		model=Task
		fields=['progress']

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


