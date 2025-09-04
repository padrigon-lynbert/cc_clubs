from django import forms
from landing_page.models import Users
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
            'banner': 'Club Profile (optional)',
            'club_name': 'Name of the club',
            'acronym': 'Acronym',
            'adviser': 'Adviser',
            'description': 'Description (min: 30)',
            'email': 'Email',
            'year_level': 'Year Level',
            'program': 'Program',
            'constitutions_and_by_laws': 'Constitutions and By Laws',
            'acceptance_letter': 'Acceptance Letter',
            'action_plan': 'Action Plan',
            'list_of_officers': 'List of Officers',
            'calendar_of_activities': 'Calender of Activities',
        }

        widgets = {
            'banner': forms.ClearableFileInput(attrs={
                'class': 'form-control',
                'id': 'imageInput',
            }),
            'club_name': forms.TextInput(attrs={
                'class': 'form-control', 
                'maxlength': 255}),
            'description': forms.Textarea(attrs={
                'class': 'form-control',
                'minlength': 30,
            }),
            'email': forms.TextInput(attrs={
                'class': 'form-control',
                'maxlength': 255
            }),
            'year_level': forms.Select(attrs={
                'class': 'form-select',
            }),
            'program': forms.Select(attrs={
                'class': 'form-select',
            }),
            'constitutions_and_by_laws': forms.ClearableFileInput(attrs={
                'class': 'form-control'
            }),
            'acceptance_letter': forms.ClearableFileInput(attrs={
                'class': 'form-control'
            }),
            'action_plan': forms.ClearableFileInput(attrs={
                'class': 'form-control'
            }),
            'list_of_officers': forms.ClearableFileInput(attrs={
                'class': 'form-control'
            }),
            'calendar_of_activities': forms.ClearableFileInput(attrs={
                'class': 'form-control'
            }),
        }
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field in self.fields.values():
            field.required = True
        
        self.fields['banner'].required = False
        self.fields['adviser'].queryset = Users.objects.filter(role=2)

