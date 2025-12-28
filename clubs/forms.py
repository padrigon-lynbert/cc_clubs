from django import forms
from landing_page.models import Users
from .models import Clubs, ClubApplication
from django.core.exceptions import ValidationError

class ClubApplicationForm(forms.ModelForm):
    
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
            'description': 'Description',
            'email': 'Email',
            'year_level': 'Year Level',
            'program': 'Program',
            'constitutions_and_by_laws': 'Constitutions and By Laws',
            'acceptance_letter': 'Acceptance Letter',
            'action_plan': 'Action Plan',
            'list_of_officers': 'List of Officers',
            'calendar_of_activities': 'Calendar of Activities',
        }

        help_texts = {
            'banner': 'Upload a banner image for your club.',
            'club_name': 'This will be the official name of the club. Must be unique.',
            'acronym': 'Short abbreviation (e.g., ABC, IEEE). Must be unique.',
            'adviser': 'Select your club adviser from the list of instructors.',
            'description': 'Give a short description (minimum 10 words).',
            'email': 'Use a valid email address (e.g., gmail, yahoo).',
            'year_level': 'Select the applicable year level for the club.',
            'program': 'Choose the program associated with the club.',
            'constitutions_and_by_laws': 'Upload your club’s constitution document (PDF).',
            'acceptance_letter': 'Upload the official acceptance letter.',
            'action_plan': 'Upload the club’s action plan (PDF).',
            'list_of_officers': 'Upload a list of club officers (PDF or Excel).',
            'calendar_of_activities': 'Provide the planned calendar of activities.',
}


        widgets = {
            'banner': forms.ClearableFileInput(attrs={
                'class': 'form-control',
                'id': 'imageInput',
                'accept': 'image/jpeg,image/png'
            }),
            'club_name': forms.TextInput(attrs={
                'class': 'form-control', 
                'maxlength': 255}),
            'acronym': forms.TextInput(attrs={
                'class': 'form-control',
                'maxlength': 50,
            }),
            'adviser': forms.Select(attrs={
                'class': 'form-select',
            }),
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
                'class': 'form-control',
                'accept': '.pdf'
            }),
            'acceptance_letter': forms.ClearableFileInput(attrs={
                'class': 'form-control',
                'accept': '.pdf'
            }),
            'action_plan': forms.ClearableFileInput(attrs={
                'class': 'form-control',
                'accept': '.pdf'
            }),
            'list_of_officers': forms.ClearableFileInput(attrs={
                'class': 'form-control',
                'accept': '.pdf,.xls,.xlsx'
            }),
            'calendar_of_activities': forms.ClearableFileInput(attrs={
                'class': 'form-control',
                'accept': '.pdf,image/jpeg,image/png'
            }),
        }
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field in self.fields.values():
            field.required = True
        
        self.fields['banner'].required = False
        self.fields['adviser'].queryset = Users.objects.filter(role=2)

    def clean_club_name(self):
        club_name = self.cleaned_data['club_name'].strip()

        if Clubs.objects.filter(club_name__iexact=club_name).exists():
            raise ValidationError('Club name already exist.')
        elif ClubApplication.objects.filter(club_name__iexact=club_name, status__in=[0, 1]).exists():
            raise ValidationError('Another applicant already registered with the same name.')

        return club_name
    
    def clean_acronym(self):
        acronym = self.cleaned_data['acronym'].strip()

        if Clubs.objects.filter(acronym__iexact=acronym).exists():
            raise ValidationError('Club acronym already exist.')
        elif ClubApplication.objects.filter(acronym__iexact=acronym, status__in=[0, 1]).exists():
            raise ValidationError('Another applicant already registered with the same acronym.')
        
        return acronym
    
    def clean_adviser(self):
        adviser = self.cleaned_data['adviser']

        if adviser.role != 2:
            raise ValidationError('Selected user is not an instructor.')
        
        return adviser
    
    def clean_description(self):
        description = self.cleaned_data['description']

        if len(description) < 30:
            raise ValidationError('The description is too short.')
        
        return description
    
    def clean_email(self):
        email = self.cleaned_data['email']

        verified_emails = ['@gmail.com', '@outlook.com', '@yahoo.com']

        if not any(email.endswith(domain) for domain in verified_emails):
            raise ValidationError('Please enter a valid email.')
        
        elif Clubs.objects.filter(email__iexact=email).exists():
            raise ValidationError('Email is already used by other club.')
        elif ClubApplication.objects.filter(email__iexact=email, status__in=[0, 1]).exists():
            raise ValidationError('Another applicant already registered with the same email.')
        
        return email
    
    def clean_banner(self):
        banner = self.cleaned_data.get('banner')

        if banner:
            valid_mime_types = ['image/jpeg', 'image/png']
            if banner.content_type not in valid_mime_types:
                raise ValidationError('Unsupported file type. Only JPEG and PNG are allowed.')

            max_file_size = 5 * 1024 * 1024  # 5MB
            if banner.size > max_file_size:
                raise ValidationError('File too large. Size should not exceed 5MB.')

        return banner

    
    def clean_constitutions_and_by_laws(self):
        file = self.cleaned_data.get('constitutions_and_by_laws')

        if file:
            valid_mime_types = ['application/pdf']
            if file.content_type not in valid_mime_types:
                raise ValidationError('Only PDF files are allowed.')

            max_file_size = 10 * 1024 * 1024  # 10MB
            if file.size > max_file_size:
                raise ValidationError('File too large. Maximum size is 10MB.')

        return file
    
    def clean_list_of_officers(self):
        file = self.cleaned_data.get('list_of_officers')

        if file:
            valid_mime_types = [
                'application/pdf',
                'application/vnd.ms-excel',
                'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'
            ]
            if file.content_type not in valid_mime_types:
                raise ValidationError('Only PDF, XLS, or XLSX files are allowed.')

            max_file_size = 10 * 1024 * 1024  # 10MB
            if file.size > max_file_size:
                raise ValidationError('File too large. Max size is 10MB.')

        return file
    
    def clean_acceptance_letter(self):
        file = self.cleaned_data.get('acceptance_letter')

        if file:
            valid_mime_types = ['application/pdf']
            if file.content_type not in valid_mime_types:
                raise ValidationError('Only PDF files are allowed.')

            max_file_size = 10 * 1024 * 1024  # 10MB
            if file.size > max_file_size:
                raise ValidationError('File too large. Maximum size is 10MB.')

        return file
    
    def clean_action_plan(self):
        file = self.cleaned_data.get('action_plan')

        if file:
            valid_mime_types = ['application/pdf']
            if file.content_type not in valid_mime_types:
                raise ValidationError('Only PDF files are allowed.')

            max_file_size = 10 * 1024 * 1024  # 10MB
            if file.size > max_file_size:
                raise ValidationError('File too large. Maximum size is 10MB.')

        return file

    def clean_calendar_of_activities(self):
        file = self.cleaned_data.get('calendar_of_activities')

        if file:
            valid_mime_types = [
                'application/pdf',
                'application/vnd.ms-excel',
                'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'
            ]
            if file.content_type not in valid_mime_types:
                raise ValidationError('Only PDF, XLS, or XLSX files are allowed.')

            max_file_size = 10 * 1024 * 1024  # 10MB
            if file.size > max_file_size:
                raise ValidationError('File too large. Max size is 10MB.')

        return file