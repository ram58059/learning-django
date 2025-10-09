from .models import Geekmodels
from django import forms

class GeeksForm(forms.ModelForm):
    class Meta:
        model = Geekmodels
        fields = ['name', 'description', 'address']