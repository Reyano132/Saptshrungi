from django.urls import path
from . import views

urlpatterns = [
	path('addService/',views.addService, name='service.addService'),
	path('servicesList/',views.ServicesList.as_view(), name='service.servicesList'),
	path('serviceDetails/<int:pk>/',views.ServiceDetails.as_view(), name='service.serviceDetails'),
    path('serviceDetails/<int:pk>/update/',views.UpdateService.as_view(), name='service.updateService'),
    path('serviceDetails/<int:pk>/delete/',views.DeleteService.as_view(), name='service.deleteService'),
    path('ajax/serviceSearch/',views.SearchService.as_view(), name='service.serviceSearch'),
]