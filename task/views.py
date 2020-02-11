from django.shortcuts import render,redirect
from .forms import CreateTaskForm,AssignTaskForm,UpdateProgress
from .models import Task
from django.views import generic
from django.urls import reverse_lazy
from user.models import User
from django.utils import timezone
from client.models import Client
from service.models import Service

def createTask(request):
	if request.method=='POST':
		form=CreateTaskForm(request.POST)
		if form.is_valid():
			task=form.save()
			return redirect('task.taskDetails',pk=task.pk)
	else:
		form=CreateTaskForm()
	return render(request,'task/createTask.html',{'form':form})

class TaskDetails(generic.DetailView):
	model=Task
	template_name='task/taskDetails.html'

class TasksList(generic.ListView):
	template_name='task/tasksList.html'
	context_object_name="tasks"
	#paginate_by = 10

	def get_queryset(self):
		return Task.objects.all().order_by('-created')

class PendingTaskList(generic.ListView):
	template_name='task/pendingtasksList.html'
	context_object_name="tasks"
	#paginate_by = 10

	def get_queryset(self):
		return Task.objects.filter(isCompleted=False).order_by('-created')

class CompletedTaskList(generic.ListView):
	template_name='task/completedtasksList.html'
	context_object_name="tasks"
	#paginate_by = 10

	def get_queryset(self):
		return Task.objects.filter(isCompleted=True).order_by('-created')


class DeleteTask(generic.DeleteView):
	model=Task
	def get_success_url(self):
		return reverse_lazy('task.tasksList')

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
	template_name='task/tasksList.html'
	context_object_name="tasks"
	paginate_by = 10

	def get_queryset(self):
		user=self.request.user
		if int(self.kwargs['pk'])==user.pk:
			user.last_seen=timezone.now()
			user.save()
		
		return Task.objects.filter(assigned_to=User.objects.get(pk=self.kwargs['pk'])).order_by('-created')


class TaskCreated(generic.ListView):
	template_name='task/tasksList.html'
	context_object_name="tasks"
	paginate_by = 10

	def get_queryset(self):
		return Task.objects.filter(service=Service.objects.get(pk=self.kwargs['pk']))

class UpdateTask(generic.UpdateView):
	model=Task
	template_name='task/updateTask.html'	
	form_class=CreateTaskForm	

class UpdateTaskProgress(generic.UpdateView):
	model=Task
	template_name='task/UpdateTaskProgress.html'	
	form_class=UpdateProgress	

class ServicesTaken(generic.ListView):
	template_name='task/tasksList.html'
	context_object_name="tasks"
	paginate_by = 10

	def get_queryset(self):
		return Task.objects.filter(for_client=Client.objects.get(pk=self.kwargs['pk']))
