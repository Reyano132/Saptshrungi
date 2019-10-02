from django.db import models
from django.contrib.auth.models import AbstractUser
from django.urls import reverse 
from django.utils import timezone


class User(AbstractUser):
	isCA=models.BooleanField(default=False)
	phone_number=models.BigIntegerField(null=True)
	birthdate=models.DateField(null=True)
	last_seen=models.DateTimeField(timezone.now(),null=True,blank=True)

	def get_absolute_url(self):		return reverse('owner.workerDetails',kwargs={'pk':self.pk})

	
	def __str__(self):
		return self.first_name+" "+self.last_name


	


