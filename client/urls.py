from django.urls import path
from . import views


urlpatterns = [
	path('registerClient/',views.registerClient, name='client.registerClient'),
	path('clientsList/',views.ClientsList.as_view(), name='client.clientsList'),
	path('clientDetails/<int:pk>/',views.ClientDetails.as_view(), name='client.clientDetails'),
    path('clientDetails/<int:pk>/update/',views.UpdateClient.as_view(), name='client.updateClient'),
    path('clientDetails/<int:pk>/delete/',views.DeleteClient.as_view(), name='client.deleteClient'),
    path('ajax/clientsSearch/',views.SearchClient.as_view(), name='client.clientsSearch'),
]