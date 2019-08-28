from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from saptshrungi.decorators import worker_required

@login_required
@worker_required
def home(request):
	return render(request,'worker/home.html',{'title':'Worker home'})
