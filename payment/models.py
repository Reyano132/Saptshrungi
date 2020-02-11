from django.db import models
from task.models import Task
from client.models import Client
from service.models import Service
from datetime import datetime  
from django.utils import timezone
from django.core.validators import MaxValueValidator, MinValueValidator
from django.urls import reverse
import uuid

class PaymentData(models.Model):
    
    for_client=models.ForeignKey(Client,on_delete=models.PROTECT,null=True,blank=True)
    for_task=models.ForeignKey(Task,on_delete=models.CASCADE)
    dated=models.DateTimeField(timezone.now(),null=True)
    value=models.IntegerField(null=True,blank=True)
    payment_method=models.CharField(max_length=30)
    card_number=models.CharField(max_length=15,null=True,blank=True)
    
	
	