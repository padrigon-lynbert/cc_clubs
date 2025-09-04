from django import forms
from .models import Clubs, ClubApplication
from django.core.exceptions import ValidationError

class ClubRegistrationForm(forms.ModelForm):
    
    class Meta:
        model = ClubApplication
        fields = ['banner', 'club_name', 'acronym', 
                  'adviser', 'description', 'email',
                  'year_level', 'program', 'constitutions_and_by_laws',
                  'acceptance_letter', 'action_plan', 'list_of_officers',
                  'list_of_officers', 'calendar_of_activities',
                  ]
        labels = {
            'banner': 'Club Profile',
            'club_name': 'Name of the club',
            'description': 'Description',
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
        }