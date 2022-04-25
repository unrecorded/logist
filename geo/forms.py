from django import forms
from geo.models import Geo

class ContactForm(forms.ModelForm):
    class Meta:
        model = Geo
        fields = "__all__"
