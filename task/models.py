from django.db import models
from user.models import User
from client.models import Client
from service.models import Service
from datetime import datetime  
from django.utils import timezone

class Task(models.Model):
	for_client=models.ForeignKey(Client,on_delete=models.PROTECT,null=True,blank=True)
	assigned_to=models.ForeignKey(User,on_delete=models.PROTECT)
	service=models.ForeignKey(Service,on_delete=models.PROTECT,null=True,blank=True)
	description=models.TextField()
	priority=models.CharField(max_length=20)
	progress=models.IntegerField(default=0)
	due_date=models.DateField(null=True)
	created=models.DateTimeField(timezone.now(),null=True,blank=True)
	modified= models.DateTimeField(timezone.now(),null=True,blank=True)
	charges=models.IntegerField(null=True,blank=True)

	def  __str__(self):
		return self.service.name
	
	def save(self, *args, **kwargs):
		''' On save, update timestamps '''
		if not self.id:
			self.created = timezone.now()
		self.modified = timezone.now()
		return super(User, self).save(*args, **kwargs)
