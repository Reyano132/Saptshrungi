from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from .forms import CustomForm
from django.contrib.auth.decorators import login_required
from saptshrungi.decorators import ca_required




@login_required
@ca_required
def home(request):
	return render(request, 'owner/home.html' )

@login_required
def redirect_page(request):
	if request.user.isCA:
		return redirect('owner.home')
	else :
		return redirect('worker.home')

def register(request):
	if request.method=='POST':
		form=CustomForm(request.POST)
		if form.is_valid():
			form.isCA=False
			form.save()
			return redirect('owner.home')
	else:
		form=CustomForm()
	return render(request,'owner/registerWorker.html',{'form':form})
