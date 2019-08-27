from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm

def register(request):
	if request.method=='POST':
		form=UserCreationForm(request.POST)
		if form.isvalid():
			form.save()
			return redirect('owner_home')
	else:
		form=UserCreationForm()
	return redirect('owner_home')
	#return render(request,'user/register.html',{'form':form})
