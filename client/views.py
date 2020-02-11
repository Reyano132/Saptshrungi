from django.shortcuts import render,redirect
from .models import Client
from .forms import ClientRegisterForm
from django.views import generic
from django.http import JsonResponse
from django.urls import reverse_lazy
from django.db.models import Q
from django.core import serializers

def registerClient(request):
	if request.method=='POST':
		form=ClientRegisterForm(request.POST)
		if form.is_valid():
			client=form.save()
			return redirect('client.clientDetails',pk=client.pk)
	else:
		form=ClientRegisterForm()
	return render(request,'client/registerClient.html',{'form':form})


class ClientsList(generic.ListView):
	template_name='client/clientsList.html'
	context_object_name="clients"
	paginate_by = 10

	def get_queryset(self):
		return Client.objects.all()

class ClientDetails(generic.DetailView):
	model=Client
	template_name='client/clientDetails.html'

class UpdateClient(generic.UpdateView):
	model=Client
	template_name='client/updateClient.html'		
	fields = ['first_name','middle_name','last_name','phone_number','email','birthdate','address','aadhar_number','pan_number']


class DeleteClient(generic.DeleteView):
	model=Client
	success_url = reverse_lazy('owner.clientsList')

class SearchClient(generic.View):
	def get(self,request):
		q=request.GET.get('q')
		clients_data=Client.objects.filter(Q(first_name__icontains=q) | Q(middle_name__icontains=q) | Q(last_name__icontains=q))
		clients=serializers.serialize("json", clients_data,fields=('pk','first_name','middle_name','last_name'))
		data={'clients':clients}
		return JsonResponse(data)