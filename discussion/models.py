from django.db import models
from task.models import Task
from user.models import User
from django.utils import timezone

class Discussion(models.Model):
	task_id=models.ForeignKey(Task,on_delete=models.CASCADE)
	sent_by=models.ForeignKey(User,on_delete=models.CASCADE)
	content=models.TextField()
	created=models.DateTimeField()

	def save(self, *args, **kwargs):
		''' On save, update timestamps '''
		if not self.id:
			self.created = timezone.now()
		return super(Discussion, self).save(*args, **kwargs)


