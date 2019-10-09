from django.urls import path
from . import views

urlpatterns = [
	path('createTask/',views.createTask, name='task.createTask'),
	path('taskDetails/<int:pk>/',views.TaskDetails.as_view(), name='task.taskDetails'),
    path('taskDetails/<int:pk>/delete',views.DeleteTask.as_view(), name='task.deleteTask'),
    path('taskDetails/<int:pk>/update',views.UpdateTask.as_view(), name='task.updateTask'),
    path('taskDetails/<int:pk>/updateProgress',views.UpdateTaskProgress.as_view(), name='task.updateTaskProgress'),
    path('tasksList/',views.TasksList.as_view(), name='task.tasksList'),
    path('workerDetails/<int:pk>/assignTask',views.assignTaskToWorker, name='task.assignTask'),
    path('workerDetails/<int:pk>/showAssignedTask',views.AssignedTasksList.as_view(), name='task.assignedTaskList'),
    path('clientDetails/<int:pk>/servicesTaken',views.ServicesTaken.as_view(), name='task.servicesTaken'),
    path('serviceDetails/<int:pk>/taskCreated',views.TaskCreated.as_view(), name='task.taskCreated'),
]