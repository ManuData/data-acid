

from django import forms
from .models import LeadsForm

class LeadsForm(forms.ModelForm):
    SALARY_RANGES = [
        ('','Select your range'),
        ('0K-30K', '0K-30K'),
        ('30K-60K', '30K-60K'),
        ('60K-more', '60K-More'),
    ]
    salary_range = forms.ChoiceField(choices=SALARY_RANGES)
    class Meta:
        model = LeadsForm
        fields = ['profession', 'salary_range','email']
        
        
    


        

