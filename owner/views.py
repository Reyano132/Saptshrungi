from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from .forms import CustomForm


def home(request):
	return render(request, 'owner/home.html' )

def register(request):
	if request.method=='POST':
		form=CustomForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('owner.home')
	else:
		form=CustomForm()
	return render(request,'owner/registerCA.html',{'form':form})
