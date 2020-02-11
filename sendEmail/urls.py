from django.urls import path
from . import views

urlpatterns = [
	path('sendEmail/<int:cq>/<int:tq>/',views.sendEmail, name='sendEmail.sendmail'),
]
