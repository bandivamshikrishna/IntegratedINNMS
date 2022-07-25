from django import forms
from .models import Menu, Rules, WorkerDetails


class WorkerDetailsForm(forms.ModelForm):
    class Meta:
        model=WorkerDetails
        fields='__all__'


class MenuForm(forms.ModelForm):
    class Meta:
        model=Menu
        fields='__all__'


class RulesForm(forms.ModelForm):
    class Meta:
        model=Rules
        fields=['rules']