# forms.py
from django import forms
from .models import *

class PhotoForm(forms.ModelForm):
    Img=forms.ImageField(required=False)
    class Meta:
	    model = photo
	    fields = ['Img']
