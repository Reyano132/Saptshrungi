from django.db import models
from task.models import Task
from client.models import Client
from service.models import Service
from datetime import datetime  
from django.utils import timezone
from user.models import User

class ReportData(models.Model):
    
    client_name=models.ForeignKey(Client,on_delete=models.PROTECT,null=True,blank=True)
    task_name=models.ForeignKey(Task,on_delete=models.CASCADE,null=True,blank=True)
    from_date=models.DateTimeField(timezone.now(),null=True)
    to_date=models.DateTimeField(timezone.now(),null=True)
    employee_name=models.ForeignKey(User,on_delete=models.CASCADE,null=True,blank=True)

    
	
	