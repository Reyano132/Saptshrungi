from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('profile/', views.home, name='owner.home'),
    path('registerWorker/',views.registerWorker, name='owner.registerWorker'),
    path('registerClient/',views.registerClient, name='owner.registerClient'),
    path('createTask/',views.createTask, name='owner.createTask'),
    path('workersList/',views.WorkersList.as_view(), name='owner.workersList'),
    path('workerDetails/<int:pk>/',views.WorkerDetails.as_view(), name='owner.workerDetails'),
    path('workerDetails/<int:pk>/assignTask',views.assignTaskToWorker, name='owner.assignTask'),
    path('workerDetails/<int:pk>/showAssignedTask',views.AssignedTasksList.as_view(), name='owner.assignedTaskList'),
    path('workerDetails/<int:pk>/update/',views.UpdateWorker.as_view(), name='owner.updateWorker'),
    path('workerDetails/<int:pk>/delete/',views.DeleteWorker.as_view(), name='owner.deleteWorker'),
    path('clientsList/',views.ClientsList.as_view(), name='owner.clientsList'),
    path('clientDetails/<int:pk>/',views.ClientDetails.as_view(), name='owner.clientDetails'),
    path('clientDetails/<int:pk>/update/',views.UpdateClient.as_view(), name='owner.updateClient'),
    path('clientDetails/<int:pk>/delete/',views.DeleteClient.as_view(), name='owner.deleteClient'),
    path('clientDetails/<int:pk>/servicesTaken',views.ServicesTaken.as_view(), name='owner.servicesTaken'),
    path('ajax/clientsSearch/',views.SearchClient.as_view(), name='owner.clientsSearch'),
    path('redirect/',views.redirect_page,name='owner.redirect-page'),
    path('servicesList/',views.ServicesList.as_view(), name='owner.servicesList'),
    path('addService/',views.addService, name='owner.addService'),
    path('',views.CustomLoginView.as_view(template_name='user/login.html'), name='login'),
    path('serviceDetails/<int:pk>/',views.ServiceDetails.as_view(), name='owner.serviceDetails'),
    path('serviceDetails/<int:pk>/update/',views.UpdateService.as_view(), name='owner.updateService'),
    path('serviceDetails/<int:pk>/delete/',views.DeleteService.as_view(), name='owner.deleteService'),
    path('serviceDetails/<int:pk>/taskCreated',views.TaskCreated.as_view(), name='owner.taskCreated'),
    path('ajax/serviceSearch/',views.SearchService.as_view(), name='owner.serviceSearch'),
    path('taskDetails/<int:pk>/',views.TaskDetails.as_view(), name='owner.taskDetails'),
    path('taskDetails/<int:pk>/delete',views.DeleteTask.as_view(), name='owner.deleteTask'),
    path('tasksList/',views.TasksList.as_view(), name='owner.tasksList'),
]