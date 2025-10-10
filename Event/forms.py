
from django.forms import *

from .models import Event
from django import forms

class DateInput(forms.DateInput):
    
    input_type='date'

class EventForm(ModelForm):
    
    class Meta:
        model=Event
        fields ="__all__"
        
        exclude= ('participant','state','nbr_participants',)
        
        widgets={'evt_date':DateInput(),} 