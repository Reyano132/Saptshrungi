from django.shortcuts import render
from .models import ReportData
from .forms import GenerateReportForm
from task.models import Task
from io import BytesIO
from xhtml2pdf import pisa
from django.template.loader import get_template
from django.template import Context
from django.http import HttpResponse
from client.models import Client
from user.models import User

def render_to_pdf(template_src, context_dict={}):
    template = get_template(template_src)
    html  = template.render(context_dict)
    result = BytesIO()
    pdf = pisa.pisaDocument(BytesIO(html.encode("ISO-8859-1")), result)
    if not pdf.err:
        return HttpResponse(result.getvalue(), content_type='application/pdf')
    return None


def getReport(request):
	if request.method=='POST':
		from_date=request.POST.get('from_date')
		to_date=request.POST.get('to_date')
		print(from_date,to_date)
		tasks=[]
		if (request.POST.get('client_name')!='' and request.POST.get('employee_name')!=''):
			client=Client.objects.get(pk=request.POST.get('client_name'))
			emp=User.objects.get(pk=request.POST.get('employee_name'))
			tasks=Task.objects.filter(created__gte=from_date,created__lte=to_date,
				assigned_to=emp,for_client=client)
		elif (request.POST.get('client_name')=='' and request.POST.get('employee_name')!=''):
			emp=User.objects.get(pk=request.POST.get('employee_name'))
			tasks=Task.objects.filter(created__gte=from_date,created__lte=to_date,
				assigned_to=emp)
		elif (request.POST.get('client_name')!='' and request.POST.get('employee_name')==''):
			client=Client.objects.get(pk=request.POST.get('client_name'))
			tasks=Task.objects.filter(created__gte=from_date,created__lte=to_date,
				for_client=client)
		else:
			tasks=Task.objects.filter(created__gte=from_date,created__lte=to_date)
		print(tasks)
		data=['fdg','fdg']
		return render_to_pdf(
            'report/pdfTemplate.html',
            {
                'pagesize':'A4',
                'tasks': tasks,
            }
        )
	else:
		form=GenerateReportForm()
	return render(request,'report/getReport.html',{'form':form})

'''

class GeneratePdf(View):
	def get(self, request,pk, *args, **kwargs):
		from_date=request.GET.get('form_date')
		to_date=request.GET.get('to_date')
		client=request.GET.get('client')
		task=request.GET.get('task')
		emp=request.GET.get('emp')

		report_data=Task.objects.filter(created__gte=from_date,created__lte=to_date,
			for_client=client,task=service,assigned_to=emp)
'''