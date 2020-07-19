from django.forms import ModelForm
from django import forms
from .models import *
from django.core import validators

def checkforpeople(value):
    if value>5:
        raise forms.ValidationError("residents are more than allowed")


class HostForm(forms.ModelForm):
    no_of_people=forms.IntegerField(validators=[checkforpeople])
    
    class Meta:
        model = Host
        fields = '__all__'
        
    def clean_name(self):
        name=self.cleaned_data.get("name")
        if (name==""):
            raise forms.ValidationError("this field should be filled")

   


class VisitorForm(ModelForm):
    class Meta:
        model = Visitor
        fields = '__all__'
        
        
  

class VisitDetailsForm(ModelForm):
    class Meta:
        model = VisitDetails
        fields = '__all__'



class EventForm(ModelForm):
    class Meta:
        model = Event
        fields ='__all__'

class EventVisitorForm(ModelForm):
    class Meta:
        model = EventVisitor
        fields = '__all__'