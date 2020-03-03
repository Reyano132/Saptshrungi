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
# Create your views here.

def createPayment(request,pk):
	if request.method=='POST':
		form=CreatePaymentForm(request.POST)
		if form.is_valid():
			payment=form.save()
			#print('ghfjhgjghjg',payment.pk)
			#return redirect('payment.PaymentDetails',pk=payment.pk)
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


class PaymentDetails(generic.DetailView):
	model=PaymentData
	template_name='payment/paymentDetails.html'
	fields = ['for_client', 'for_task','dated','value','payment_method']


class GeneratePdf(View):
	def get(self, request,pk, *args, **kwargs):
		template=get_template('payment/invoice.html')
		p=PaymentData.objects.get(pk=pk)
		data = {
			'today': 'monday', 
			'amount': '200',
			'customer_name': p.for_client ,
			'order_id': '123',
		}
		#html = template.render(data)
		pdf = render_to_pdf('payment/invoice.html', data)
		return HttpResponse(pdf, content_type='application/pdf')
