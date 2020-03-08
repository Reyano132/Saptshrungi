from django.urls import path
from . import views

urlpatterns = [
    path('createPayment/<int:pk>/',views.createPayment, name='payment.CreatePayment'),
    path('paymentsForClient/<int:pk>',views.getPaymentsForClient, name='payment.PaymentsForClient'),
    path('paymentsForTask/<int:pk>',views.getPaymentsForTask, name='payment.PaymentsForTask'),
    path('invoice/<int:pk>/',views.GeneratePdf.as_view(), name='payment.generatePDF'),
]