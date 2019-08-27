from django.shortcuts import render

def home(request):
	return render(request,'worker/home.html',{'title':'Worker home'})
