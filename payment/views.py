from django.shortcuts import render, redirect
from .forms import CreatePaymentForm
from .models import PaymentData
from django.views import generic
from django.urls import reverse_lazy
from user.models import User
from django.utils import timezone
from client.models import Client
from service.models import Service
from task.models import Task
from django.http import HttpResponse
from django.views.generic import View
from saptshrungi.utils import render_to_pdf 
from django.template.loader import get_template
from django.utils import timezone
import datetime
# Create your views here.

def createPayment(request,pk):
	if request.method=='POST':
		form=CreatePaymentForm(request.POST)
		if form.is_valid():
			print(form.cleaned_data['dated'])
			payment=form.save()
			return redirect('payment.generatePDF',pk=payment.pk)
	else:
		form=CreatePaymentForm()
		t=Task.objects.filter(pk=pk)
		c=0
		for i in t:
			c=i.for_client.pk
		form.fields['for_client'].queryset=Client.objects.filter(pk=c)
		form.fields['for_task'].queryset=t
	return render(request,'payment/createPayment.html',{'form':form})


def getPaymentsForClient(request,pk):
	payments=PaymentData.objects.filter(for_client=Client.objects.get(pk=pk))
	return render(request,'payment/clientPaymentDetails.html',{'payments':payments})

def getPaymentsForTask(request,pk):
	payments=PaymentData.objects.filter(for_task=Task.objects.get(pk=pk))
	return render(request,'payment/paymentDetails.html',{'payments':payments,'taskid':pk})


class GeneratePdf(View):
	def get(self, request,pk, *args, **kwargs):
		template=get_template('payment/invoice.html')
		p=PaymentData.objects.get(pk=pk)
		print('pdg',p.dated.date())
		data = {
			'today': p.dated.date(), 
			'amount': p.value,
			'customer_name': p.for_client ,
			'order_id': p.pk+1000,
		}
		#html = template.render(data)
		pdf = render_to_pdf('payment/invoice.html', data)
		return HttpResponse(pdf, content_type='application/pdf')
