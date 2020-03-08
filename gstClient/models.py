from django.db import models
from user.models import User
from client.models import Client
from service.models import Service
from datetime import datetime  
from django.utils import timezone
from django.core.validators import MaxValueValidator, MinValueValidator
from django.urls import reverse
from service.models import Service
import datetime
from django.core.validators import MaxValueValidator, MinValueValidator

def current_year():
    return datetime.date.today().year

def max_value_current_year(value):
    return MaxValueValidator(current_year())(value) 


class GSTType(models.Model):
    gst_type=models.ForeignKey(Service,on_delete=models.CASCADE)
    def __str__(self):
        return self.gst_type.name

class GSTClient(models.Model):
    client=models.ForeignKey(Client,on_delete=models.PROTECT,null=True,blank=True)
    month=models.TextField(null=True)
    year = models.IntegerField(('year'), validators=[MinValueValidator(1984), max_value_current_year])
    gst_type=models.ForeignKey(GSTType,on_delete=models.PROTECT,null=True,blank=True)
	
