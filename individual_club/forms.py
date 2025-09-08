from django import forms
from django.core.exceptions import ValidationError
from landing_page.models import Users
from clubs.models import MemberApplication

class MembershipApplicationForm(forms.ModelForm):

    class Meta:
        model = MemberApplication
        fields = [
            'certificate_of_recognition', 'response_text'
        ]

        labels = {
            'certificate_of_recognition': 'Certificate of Recognition (max: 2mb)',
            'response_text': 'Reason to join club (optional)',
        }

        widgets = {
            'certificate_of_recognition': forms.ClearableFileInput(attrs={
                'class': 'form-control',
            }),
            'response_text': forms.Textarea(attrs={
                'class': 'form-control',
                'maxlength': 255,
            })
        }

    def __init__(self, *args, **kwargs):
        super.__init__(*args, **kwargs)
        self.fields['certificate_of_recognition'].required = True

    def clean_certificate_of_recognition(self):
        cor = self.cleaned_data.get('certificate_of_recognition')
        mb = 1024 * 1024
        if cor:
            if cor.size > 2 * mb:
                raise ValidationError(f'Your file size {round(cor.size / mb, 2)} MB exceeds 2MB.')
        
        return cor