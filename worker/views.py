from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from saptshrungi.decorators import worker_required
from .forms import WorkerRegisterForm
from user.models import User
from django.views import generic
from django.urls import reverse_lazy
from task.models import Task
import datetime
from django.http import JsonResponse

@login_required
@worker_required
def home(request):
	return render(request,'worker/home.html')

class getNotificationADayAhead(generic.View):
	def get(self,request):
		pk=self.request.user.pk
		tasks=list(Task.objects.filter(due_date__startswith=datetime.date.today()+datetime.timedelta(days=1), assigned_to=pk, isCompleted=False).order_by('-created'))
		#tasks=serializers.serialize("json", task_data,fields=('pk','service','for_client','assigned_to'))
		tmp=[]
		for task in tasks:
			service=task.service.name
			client=task.for_client.first_name+' '+task.for_client.middle_name+' '+task.for_client.last_name
			emp=task.assigned_to.first_name+' '+task.assigned_to.last_name
			tmp.append({'pk':task.pk,'client':client,'service':service,'emp':emp})
		data={'tasks':tmp}
		return JsonResponse(data)

class getNotificationOnDueDay(generic.View):
	def get(self,request):
		pk=self.request.user.pk
		tasks=list(Task.objects.filter(due_date__startswith=datetime.date.today(),assigned_to=pk, isCompleted=False).order_by('-created'))
		#tasks=serializers.serialize("json", task_data,fields=('pk','service','for_client','assigned_to'))
		tmp=[]
		for task in tasks:
			service=task.service.name
			client=task.for_client.first_name+' '+task.for_client.middle_name+' '+task.for_client.last_name
			emp=task.assigned_to.first_name+' '+task.assigned_to.last_name
			tmp.append({'pk':task.pk,'client':client,'service':service,'emp':emp})
		data={'tasks':tmp}
		return JsonResponse(data)

class Profile(generic.ListView):
	template_name='worker/home.html'
	context_object_name="tasks"

	def get_queryset(self):
		pk=self.request.user.pk
		return Task.objects.filter(due_date__startswith=datetime.date.today()+datetime.timedelta(days=1) , assigned_to=pk, isCompleted=False).order_by('-created')

def registerWorker(request):
	if request.method=='POST':
		form=WorkerRegisterForm(request.POST)
		if form.is_valid():
			form.isCA=False
			worker=form.save()
			return redirect('worker.workerDetails',pk=worker.pk)
	else:
		form=WorkerRegisterForm()
	return render(request,'worker/registerWorker.html',{'form':form})


class WorkersList(generic.ListView):
	template_name='worker/workersList.html'
	context_object_name="workers"
	paginate_by = 10

	def get_queryset(self):
		return User.objects.filter(isCA=False)

class WorkerDetails(generic.DetailView):
	model=User
	template_name='worker/workerDetails.html'	

class UpdateWorker(generic.UpdateView):
	model=User
	template_name='worker/updateWorker.html'		
	fields = ['first_name','last_name','phone_number','email','birthdate']

class DeleteWorker(generic.DeleteView):
	model=User
	success_url = reverse_lazy('worker.workersList')

