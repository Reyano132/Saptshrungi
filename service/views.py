from django.shortcuts import render, redirect
from .models import Service
from .forms import AddServiceForm
from django.views import generic
from django.http import JsonResponse
from django.urls import reverse_lazy
from django.core import serializers

def addService(request):
	if request.method=='POST':
		form=AddServiceForm(request.POST)
		if form.is_valid():
			service=form.save()
			return redirect('service.serviceDetails',pk=service.pk)
	else:
		form=AddServiceForm()
	return render(request,'service/addService.html',{'form':form})

class ServicesList(generic.ListView):
	template_name='service/serviceList.html'
	context_object_name="services"
	paginate_by = 10

	def get_queryset(self):
		return Service.objects.all()

class ServiceDetails(generic.DetailView):
	model=Service
	template_name='service/serviceDetails.html'

class UpdateService(generic.UpdateView):
	model=Service
	template_name='service/updateService.html'		
	fields = ['name', 'description','documents']

class DeleteService(generic.DeleteView):
	model=Service
	success_url = reverse_lazy('service.servicesList')

class SearchService(generic.View):
	def get(self,request): 
		q=request.GET.get('q')
		services_data=Service.objects.filter(name__icontains=q)
		services=serializers.serialize("json", services_data,fields=('pk','name'))
		data={'services':services}
		return JsonResponse(data)