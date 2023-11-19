

from django import forms
from .models import LeadsForm

class LeadsForm(forms.ModelForm):
    class Meta:
        model = LeadsForm
        fields = ['profesion', 'salary_range']
