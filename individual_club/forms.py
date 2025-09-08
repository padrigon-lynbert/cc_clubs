from django.forms import forms
from django.core.exceptions import ValidationError
from landing_page.models import Users
from clubs.models import MemberApplication

class MembershipApplicationForm(forms.ModelForm):

    class Meta:
        model = MemberApplication
