from django.db import models
from user.models import User
from client.models import Client
from service.models import Service
from datetime import datetime  
from django.utils import timezone
from django.core.validators import MaxValueValidator, MinValueValidator
from django.urls import reverse

class Task(models.Model):
	for_client=models.ForeignKey(Client,on_delete=models.PROTECT,null=True,blank=True)
	assigned_to=models.ForeignKey(User,on_delete=models.PROTECT)
	service=models.ForeignKey(Service,on_delete=models.PROTECT,null=True,blank=True)
	description=models.TextField()
	priority=models.CharField(max_length=20)
	progress=models.PositiveIntegerField(default=0, validators=[MinValueValidator(0), MaxValueValidator(100)])
	due_date=models.DateField(null=True)
	created=models.DateTimeField(timezone.now(),null=True)
	modified= models.DateTimeField(timezone.now(),null=True,blank=True)
	charges=models.IntegerField(null=True,blank=True)

	def  __str__(self):
		return self.service.name
	
	def save(self, *args, **kwargs):
		''' On save, update timestamps '''
		if not self.id:
			self.created = timezone.now()
		self.modified = timezone.now()
		return super(Task, self).save(*args, **kwargs)

	def get_absolute_url(self):		
		return reverse('owner.taskDetails',kwargs={'pk':self.pk})
