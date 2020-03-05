from django.shortcuts import render
from .models import ReportData\
from Task.models import Task

def getReport(request):
	return render(request,'report/getReport.html')


class GeneratePdf(View):
	def get(self, request,pk, *args, **kwargs):
		from_date=request.GET.get('form_date')
		to_date=request.GET.get('to_date')
		client=request.GET.get('client')
		task=request.GET.get('task')
		emp=request.GET.get('emp')

		report_data=Task.objects.filter(created__gte=from_date,created__lte=to_date,
			for_client=client,task=service,assigned_to=emp)