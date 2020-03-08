from django.contrib import admin
from .models import GSTClient,GSTType

admin.site.register(GSTType)
admin.site.register(GSTClient)
