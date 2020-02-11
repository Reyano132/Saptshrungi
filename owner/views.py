from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from .forms import WorkerRegisterForm,ClientRegisterForm,AddServiceForm,CreateTaskForm,AssignTaskForm,UpdateProgress
from django.contrib.auth.decorators import login_required
from saptshrungi.decorators import ca_required
from django.contrib.auth.views import LoginView
from client.models import Client
from user.models import User
from service.models import Service
from django.views import generic
from django.http import JsonResponse,HttpResponse
from django.core import serializers
from django.db.models import Q
from django.urls import reverse_lazy
from task.models import Task
from django.views.decorators.csrf import csrf_protect
from django.utils import timezone
import datetime



@login_required
@ca_required
def home(request):
	print("fgddfg",datetime.date.today()+datetime.timedelta(days=1))
	return render(request, 'owner/home.html' )

class Home(generic.ListView):
	template_name='owner/home.html'
	context_object_name="tasks"

	def get_queryset(self):

		return Task.objects.filter(isCompleted=True).order_by('-created')

@login_required
def redirect_page(request):
	if request.user.isCA:
		return redirect('owner.home')
	else :
		return redirect('worker.home')

def registerWorker(request):
	if request.method=='POST':
		form=WorkerRegisterForm(request.POST)
		if form.is_valid():
			form.isCA=False
			worker=form.save()
			return redirect('owner.workerDetails',pk=worker.pk)
	else:
		form=WorkerRegisterForm()
	return render(request,'owner/registerWorker.html',{'form':form})

def registerClient(request):
	if request.method=='POST':
		form=ClientRegisterForm(request.POST)
		if form.is_valid():
			client=form.save()
			return redirect('owner.clientDetails',pk=client.pk)
	else:
		form=ClientRegisterForm()
	return render(request,'owner/registerClient.html',{'form':form})

def addService(request):
	if request.method=='POST':
		form=AddServiceForm(request.POST)
		if form.is_valid():
			service=form.save()
			return redirect('owner.serviceDetails',pk=service.pk)
	else:
		form=AddServiceForm()
	return render(request,'owner/addService.html',{'form':form})

def createTask(request):
	if request.method=='POST':
		form=CreateTaskForm(request.POST)
		if form.is_valid():
			task=form.save()
			return redirect('owner.taskDetails',pk=task.pk)
	else:
		form=CreateTaskForm()
	return render(request,'owner/createTask.html',{'form':form})

'''
def workerDetails(request):
	workers=User.objects.filter(isCA=False)
	return render(request,'owner/workerDetails.html',{'workers':workers})


def clientDetails(request):
	clients=
	return render(request,'owner/clientDetails.html',{'clients':clients})
'''

class ClientsList(generic.ListView):
	template_name='owner/clientsList.html'
	context_object_name="clients"
	paginate_by = 10

	def get_queryset(self):
		return Client.objects.all()

class SearchClient(generic.View):
	def get(self,request):
		q=request.GET.get('q')
		clients_data=Client.objects.filter(Q(first_name__icontains=q) | Q(middle_name__icontains=q) | Q(last_name__icontains=q))
		clients=serializers.serialize("json", clients_data,fields=('pk','first_name','middle_name','last_name'))
		data={'clients':clients}
		return JsonResponse(data)
		

class ClientDetails(generic.DetailView):
	model=Client
	template_name='owner/clientDetails.html'

class UpdateClient(generic.UpdateView):
	model=Client
	template_name='owner/updateClient.html'		
	fields = ['first_name','middle_name','last_name','phone_number','email','birthdate','address','aadhar_number','pan_number']


class DeleteClient(generic.DeleteView):
	model=Client
	success_url = reverse_lazy('owner.clientsList')
	


class WorkersList(generic.ListView):
	template_name='owner/workersList.html'
	context_object_name="workers"
	paginate_by = 10

	def get_queryset(self):
		return User.objects.filter(isCA=False)

class WorkerDetails(generic.DetailView):
	model=User
	template_name='owner/workerDetails.html'	

class UpdateWorker(generic.UpdateView):
	model=User
	template_name='owner/updateWorker.html'		
	fields = ['first_name','last_name','phone_number','email','birthdate']

class DeleteWorker(generic.DeleteView):
	model=User
	success_url = reverse_lazy('owner.workersList')


class CustomLoginView(LoginView):

	def get(self, request, *args, **kwargs):
		if self.request.user.is_authenticated and self.request.user.isCA:
			return redirect('owner.home')
		elif self.request.user.is_authenticated:
			return redirect('worker.home')
		return super(CustomLoginView, self).get(request, *args, **kwargs)

class ServicesList(generic.ListView):
	template_name='owner/serviceList.html'
	context_object_name="services"
	paginate_by = 10

	def get_queryset(self):
		return Service.objects.all()

class ServiceDetails(generic.DetailView):
	model=Service
	template_name='owner/serviceDetails.html'

class UpdateService(generic.UpdateView):
	model=Service
	template_name='owner/updateService.html'		
	fields = ['name', 'description','documents']

class DeleteService(generic.DeleteView):
	model=Service
	success_url = reverse_lazy('owner.servicesList')

class SearchService(generic.View):
	def get(self,request): 
		q=request.GET.get('q')
		services_data=Service.objects.filter(name__icontains=q)
		services=serializers.serialize("json", services_data,fields=('pk','name'))
		data={'services':services}
		return JsonResponse(data)

class TaskDetails(generic.DetailView):
	model=Task
	template_name='owner/taskDetails.html'

class TasksList(generic.ListView):
	template_name='owner/tasksList.html'
	context_object_name="tasks"
	paginate_by = 10

	def get_queryset(self):
		return Task.objects.all()

class DeleteTask(generic.DeleteView):
	model=Task
	success_url = reverse_lazy('owner.tasksList')

def assignTaskToWorker(request,pk):
	if request.method=='POST':
		form=AssignTaskForm(request.POST)
		if form.is_valid():
			task=form.save()
			return redirect('owner.taskDetails',pk=task.pk)
	else:
		form=AssignTaskForm()
		form.fields['assigned_to'].queryset=User.objects.filter(pk=pk)
	return render(request,'owner/createTask.html',{'form':form})

class AssignedTasksList(generic.ListView):
	template_name='owner/tasksList.html'
	context_object_name="tasks"
	paginate_by = 10

	def get_queryset(self):
		user=self.request.user
		if int(self.kwargs['pk'])==user.pk:
			user.last_seen=timezone.now()
			user.save()
		
		return Task.objects.filter(assigned_to=User.objects.get(pk=self.kwargs['pk']))

class ServicesTaken(generic.ListView):
	template_name='owner/tasksList.html'
	context_object_name="tasks"
	paginate_by = 10

	def get_queryset(self):
		return Task.objects.filter(for_client=Client.objects.get(pk=self.kwargs['pk']))

class TaskCreated(generic.ListView):
	template_name='owner/tasksList.html'
	context_object_name="tasks"
	paginate_by = 10

	def get_queryset(self):
		return Task.objects.filter(service=Service.objects.get(pk=self.kwargs['pk']))

class UpdateTask(generic.UpdateView):
	model=Task
	template_name='owner/updateTask.html'	
	form_class=CreateTaskForm	

class UpdateTaskProgress(generic.UpdateView):
	model=Task
	template_name='owner/UpdateTaskProgress.html'	
	form_class=UpdateProgress	
'''
def storeLastSeen(request):
	if request.is_ajax():
		message = "Yes, AJAX!"
		q=request.POST.get('q')
		user=User.objects.get(pk=q)
		user.last_seen=timezone.now()
		user.save()
	else:
		message = "Not Ajax"
	return JsonResponse({'message':message})
'''

class GetNotification(generic.View):
	def get(self,request):
		q=request.GET.get('q')
		lenght=0

		if int(q)==self.request.user.pk:
			user=User.objects.get(pk=q)
			print(user.last_seen)
			task_data=Task.objects.filter(assigned_to=User.objects.get(pk=q),created__gte=user.last_seen)
			lenght=len(task_data)
			print(lenght)

		data={'notification':lenght }
		return JsonResponse(data)