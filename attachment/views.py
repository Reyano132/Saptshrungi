from django.shortcuts import render
from .models import Attachments
from django.views.decorators.http import require_http_methods
from django.http import JsonResponse
from task.models import Task
from django.core import serializers
from task.models import Task
from django.views import generic
import os
from django.conf import settings
from django.http import HttpResponse, Http404

@require_http_methods(["POST"])
def addAttachment(request):
	id=request.POST.get('task_id')
	task_name=Task.objects.get(pk=id)
	#discussion=serializers.serialize("json", discussion_data)
	file_name=request.FILES['file']
	a=Attachments(task=task_name,file=file_name)
	a.save()
	attachment=serializers.serialize('json',[a])
	file=a.file.name.split('/')
	data={'pk':a.pk,'name':file[1]}
	return JsonResponse(data)


class GetAttachment(generic.View):
	def get(self,request): 
		q=request.GET.get('q')
		attachment_data=Attachments.objects.filter(task_id=q)
		attachment_name=[]
		
		for d in attachment_data:
			filename=d.filename().split('/')
			attachment_name.append(filename[1])

		print(attachment_name)
			
		attachment=serializers.serialize("json", attachment_data,fields=['id'])
		
		data={'attachment':attachment,'names':attachment_name}
		return JsonResponse(data)

def download(request, pk):
	attachment=Attachments.objects.get(id=pk)
	path=attachment.file.name;
	file_path = os.path.join(settings.MEDIA_ROOT, path)
	if os.path.exists(file_path):
		with open(file_path, 'rb') as fh:
			response = HttpResponse(fh.read(), content_type="application/octet-stream")
			response['Content-Disposition'] = 'inline; filename=' + os.path.basename(file_path)
			return response
	raise Http404