# forms.py
from django import forms
from .models import Teeth_Model

class ImageForm(forms.ModelForm):

    class Meta:
        model = Teeth_Model
        fields = ['name', 'phone_number', 'email', 'image']
