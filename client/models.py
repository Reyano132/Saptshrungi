from django.db import models
from django.urls import reverse

class Client(models.Model):
	first_name=models.CharField(max_length=20)
	middle_name=models.CharField(max_length=20,null=True,blank=True)
	last_name=models.CharField(max_length=20)
	email=models.EmailField(max_length=100,null=True,blank=True)
	phone_number=models.BigIntegerField(null=True,blank=True)
	birthdate=models.DateField(null=True)
	address=models.TextField()
	aadhar_number=models.BigIntegerField(null=True,blank=True)
	pan_number=models.CharField(max_length=20,blank=True)

	def get_absolute_url(self):
		return reverse('owner.clientDetails',kwargs={'pk':self.pk})

	def __str__(self):
		return self.first_name+" "+self.last_name

