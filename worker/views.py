from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from saptshrungi.decorators import worker_required
from .forms import WorkerRegisterForm
from user.models import User
from django.views import generic
from django.urls import reverse_lazy
from task.models import Task
import datetime

@login_required
@worker_required
def home(request):
	return render(request,'worker/home.html')


class Profile(generic.ListView):
	template_name='worker/home.html'
	context_object_name="tasks"

	def get_queryset(self):

		return Task.objects.filter(due_date__startswith=datetime.date.today()+datetime.timedelta(days=1)).order_by('-created')

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

