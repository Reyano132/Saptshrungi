from django.urls import path
from . import views

urlpatterns = [
	path('getGSTClient/',views.getGSTClient, name='gst.getGSTClient'),
	path('getGSTTypes/',views.getGSTType, name='gst.getGSTType'),
]