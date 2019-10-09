from django.shortcuts import render
from django.http import JsonResponse
from .models import Discussion
from django.views.decorators.http import require_http_methods
from django.utils import timezone
from django.core import serializers
from django.views import generic
from user.models import User 
from task.models import Task


class GetDiscussion(generic.View):
	def get(self,request): 
		q=request.GET.get('q')
		discussion_data=Discussion.objects.filter(task_id=q)
		senders_name=[]
		created_time=[]
		print("time: ", discussion_data[0].created.strftime("%b.%d,%Y %I.%M %p"))
		for d in discussion_data:
			senders_name.append(d.sent_by)
			created_time.append(d.created.strftime("%b.%d,%Y %I.%M %p"))
		discussion=serializers.serialize("json", discussion_data)
		senders=serializers.serialize('json',senders_name,fields=['first_name','last_name'])
		
		data={'discussion':discussion,'senders':senders,'created':created_time}
		return JsonResponse(data)

@require_http_methods(["POST"])
def addComment(request):
	n_sent_by=User.objects.get(pk=request.POST.get('sent_by'))
	n_task_id=Task.objects.get(pk=request.POST.get('task_id'))
	n_text=request.POST.get('text')
	n_created=timezone.now()
	new_comment=Discussion(sent_by=n_sent_by,task_id=n_task_id,content=n_text,created=n_created)
	new_comment.save()
	data={'created':n_created.strftime("%b.%d,%Y %I.%M %p"),'first_name':n_sent_by.first_name,
				'last_name':n_sent_by.last_name}
	return JsonResponse(data)