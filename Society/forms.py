# forms.py

from django import forms
from django import forms
from .models import Society

class SocietyRegistrationForm(forms.ModelForm):
    class Meta:
        model = Society
        fields = ['name', 'address']

# forms.py

# forms.py

from django import forms

class ResidentUIDForm(forms.Form):
    resident_uid = forms.UUIDField(label='Enter your Resident UID')

from django import forms
from .models import ResidentProblem


class ResidentProblemForm(forms.ModelForm):
    class Meta:
        model = ResidentProblem
        fields = ['problem_description','room_number','phone_number']

