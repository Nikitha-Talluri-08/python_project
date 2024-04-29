from django import forms
from .models import Userregistration
from .models import VisaApplication

class UserregistrationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    repassword = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = Userregistration
        fields = "__all__"
        exclude = ["id"]

# forms.py

class VisaApplicationForm(forms.ModelForm):
    class Meta:
        model = VisaApplication
        fields = ['passport_number', 'country_of_origin', 'purpose_of_visit']

