from django.forms import forms
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

