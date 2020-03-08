from django.shortcuts import render
from .forms import GetGSTClientForm
from .models import GSTType,GSTClient
from client.models import Client

def getGSTClient(request):
	if request.method=='POST':
		form=GetGSTClientForm(request.POST)
		if form.is_valid():
			fmonth=form.cleaned_data['month']
			fyear=form.cleaned_data.get("year")
			fgst_type=form.cleaned_data.get("gst_type")
			tmp=GSTClient.objects.filter(month=fmonth,year=fyear,gst_type=fgst_type)
			completed_clients=[]
			for t in tmp:
				completed_clients.append(t.client)
			tmp=Client.objects.filter(isGSTClient=True)
			incompleted_clients=[]
			for t in tmp:
				if t not in completed_clients:
					incompleted_clients.append(t)

			print(completed_clients,' ',incompleted_clients)

		return render(request,'gstClient/gstClientsData.html',
				{'completed_clients':completed_clients,'incompleted_clients':incompleted_clients})
	else:
		form=GetGSTClientForm()
	return render(request,'gstClient/gstReport.html',{'form':form})

def getGSTType(request):
		types=GSTType.objects.all()
		print(types)
		return render(request,'gstClient/gstType.html',{'types':types})
