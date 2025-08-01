from django import forms
from .models import ClubApplication

class ClubRegistrationForm(forms.ModelForm):
    
    class Meta:
        model = ClubApplication
        fields = ['club_name', 'description']
        labels = {
            'club_name': 'Name of the club',
            'description': 'Description'
        }
        widgets = {
            'club_name': forms.TextInput(attrs={
                'class': 'form-control', 
                'maxlength': 255}),
            'description': forms.Textarea(attrs={
                'class': 'form-control'}),
        }