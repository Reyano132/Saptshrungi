from django.urls import path
from . import views

urlpatterns = [
	path('ajax/addAttachment/',views.addAttachment, name='attachment.addAttachment'),
	path('ajax/getAttachment/',views.GetAttachment.as_view(), name='attachment.getAttachment'),
	path('downloadAttachment/<int:pk>/',views.download, name='attachment.downloadAttachment'),
]	