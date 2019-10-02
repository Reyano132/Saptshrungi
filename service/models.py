from django.db import models
from django.urls import reverse
from django_mysql.models import ListCharField


# Create your models here.
class Service(models.Model):
	name=models.CharField(max_length=100)
	description=models.TextField(null=True,blank=True)
	documents=ListCharField(
		base_field=models.CharField(max_length=100),
		size=10,
		max_length=(100 * 30),
		null=True,blank=True
    )
	def get_absolute_url(self):
		return reverse('owner.serviceDetails',kwargs={'pk':self.pk})

	def __str__(self):
		return self.name