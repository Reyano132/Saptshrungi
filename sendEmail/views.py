from django.shortcuts import render, redirect
from saptshrungi.settings import EMAIL_HOST_USER
from django.core.mail import send_mail
from client.models import Client
from task.models import Task
from django.contrib import messages
# Create your views here.
#DataFlair #Send Email
def sendEmail(request, cq, tq):
    #sub = forms.Subscribe()
    
    #sub = forms.(request.POST)
    subject = str(Task.objects.get(pk=tq).service)+"-Completed"
    message = 'task is completed'
    recepient = str(Client.objects.get(pk=cq).email)
    send_mail(subject, message, EMAIL_HOST_USER, [recepient], fail_silently = False)
    print(subject,' ',messages,' ',recepient)
    messages.info(request, 'Mail successfully sent to '+ str(Client.objects.get(pk=cq).email))
    task=Task.objects.get(pk=tq)
    task.isCompleted=True
    task.save()
    return redirect(request.META['HTTP_REFERER'])
       

