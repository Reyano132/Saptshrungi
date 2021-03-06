from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('profile/', views.home, name='worker.home'),
    path('registerWorker/',views.registerWorker, name='worker.registerWorker'),
    path('workersList/',views.WorkersList.as_view(), name='worker.workersList'),
    path('workerDetails/<int:pk>/',views.WorkerDetails.as_view(), name='worker.workerDetails'),
    path('workerDetails/<int:pk>/update/',views.UpdateWorker.as_view(), name='worker.updateWorker'),
    path('workerDetails/<int:pk>/delete/',views.DeleteWorker.as_view(), name='worker.deleteWorker'),
    path('ajax/getNotificationADayAhead/',views.getNotificationADayAhead.as_view()),
    path('ajax/getNotificationOnDueDay/',views.getNotificationOnDueDay.as_view()),
]