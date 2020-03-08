from django import forms
from .models import GSTClient,GSTType
import datetime
from client.models import Client


def current_year():
    return datetime.date.today().year

def year_choices():
    return [(r,r) for r in range(1984, datetime.date.today().year+1)]

class GetGSTClientForm(forms.ModelForm):
    year = forms.TypedChoiceField(coerce=int, choices=year_choices, initial=current_year)
    month= forms.ChoiceField(choices=[(x,x) for x in ['January','February', 'March', 
                        'April','May','June','July','August','September','October','November','December']])
    gst_client=Client.objects.filter(isGSTClient=True)
    class Meta:
        model=GSTClient
        fields=['month','year','gst_type']