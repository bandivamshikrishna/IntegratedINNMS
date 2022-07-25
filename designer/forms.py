from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Designer, RoomCustomization


class DesignerUserForm(UserCreationForm):
    class Meta:
        model=User
        fields=['first_name','last_name','email','username']



class DesignerForm(forms.ModelForm):
    class Meta:
        model=Designer
        fields=['gender','profile_pic','resume']

    

class DesignerUserUpdateForm(forms.ModelForm):
    class Meta:
        model=User
        fields=['first_name','last_name','email']

    

class DesignerUpdateForm(forms.ModelForm):
    class Meta:
        model=Designer
        fields=['gender','profile_pic']


class RoomCustomizationForm(forms.ModelForm):
    class Meta:
        model=RoomCustomization
        fields=['left','right','top','bottom','front','back']

    
class RoomPriceThemeForm(forms.ModelForm):
    class Meta:
        model=RoomCustomization
        fields=['price','theme']


class RoomPriceForm(forms.ModelForm):
    class Meta:
        model=RoomCustomization
        fields=['price']