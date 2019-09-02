from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='owner.home'),
    path('register/',views.register, name='owner.register'),
    path('forRedirect/',views.redirect_page,name='redirect-page')
]