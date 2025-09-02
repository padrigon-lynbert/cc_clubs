from django import forms
from .models import ClubApplication

class ClubRegistrationForm(forms.ModelForm):
    
    class Meta:
        model = ClubApplication
        fields = ['banner', 'club_name', 'description', 'location']
        labels = {
            'banner': 'Club Profile',
            'club_name': 'Name of the club',
            'description': 'Description',
            'location': 'Club Location',
        }
        widgets = {
            'banner': forms.ClearableFileInput(attrs={
                'class': 'form-control',
                'id': 'imageInput',}),
            'club_name': forms.TextInput(attrs={
                'class': 'form-control', 
                'maxlength': 255}),
            'description': forms.Textarea(attrs={
                'class': 'form-control'}),
            'location': forms.Select(attrs={
                'class': 'form-control'}),
        }