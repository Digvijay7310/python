from django import forms
from .models import ChaiVarity

class ChaiVarityForms(forms.Form):
    chai_varity = forms.ModelChoiceField(queryset=ChaiVarity.objects.all(), label="Select chai variety")