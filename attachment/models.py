from django.db import models
from task.models import Task
import os 

def attachment_directory_path(instance, filename):
    return 'task_{0}/{1}'.format(instance.task.id, filename)

class Attachments(models.Model):
	task=models.ForeignKey(Task,on_delete=models.CASCADE)
	file=models.FileField(upload_to=attachment_directory_path)

	def filename(self):
		filename=str(self.file.name)
		return filename
