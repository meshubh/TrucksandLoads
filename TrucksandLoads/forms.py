
from django.contrib.auth.models import *
from models import *
from django import forms


class TruckForm(forms.ModelForm):
    class Meta:
        model=Trucks
        fields={'truck_company_name','truck_type','start_point','end_point',}

    def __init__(self, *args, **kwargs):
        super(TruckForm, self).__init__(*args, **kwargs)
        self.fields.keyOrder = ['truck_company_name','truck_type','start_point','end_point']


class LoadForm(forms.ModelForm):
    class Meta:
        model=Load
        #widgets = {'type': forms.RadioSelect}
        fields={'type','start_point','end_point',}

