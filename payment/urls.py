from django.urls import path
from . import views

urlpatterns = [
    path('createPayment/<int:pk>/',views.createPayment, name='payment.CreatePayment'),
    path('PaymentDetails/<int:pk>/',views.PaymentDetails.as_view(), name='payment.PaymentDetails'),
    path('invoice/<int:pk>/',views.GeneratePdf.as_view(), name='payment.generatePDF'),
]