from django.db import models
from django.urls import reverse


# Create your models here.
class Service(models.Model):
	name=models.CharField(max_length=100)
	description=models.TextField(null=True,blank=True)
	documents=models.TextField(null=True,blank=True)

	def get_absolute_url(self):
		return reverse('owner.serviceDetails',kwargs={'pk':self.pk})

	def __str__(self):
		return self.name