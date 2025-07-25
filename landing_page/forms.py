from django import forms
from .models import Memberships

class RegisterClubForm(forms.ModelForm):
    
    class Meta:
        model = Memberships
        fields = ['club']
        labels = {'club': 'Choose a club'}
        widgets = {'club': forms.Select(attrs={'class': 'form-control'})}