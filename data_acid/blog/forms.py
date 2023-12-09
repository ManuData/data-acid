

from django import forms
from .models import LeadsForm

class LeadsForm(forms.ModelForm):
    class Meta:
        model = LeadsForm
        fields = ['profession', 'salary_range','email']
        widgets = {
            'salary_range': forms.TextInput(attrs={'type': 'number', 'min': '0', 'oninput': 'validity.valid||(value="");'})
        }

