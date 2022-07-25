from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Customer, CustomerComplaint, CustomerRoomCustomization, HostelCustomer
from django.contrib.admin.widgets import AdminDateWidget
import datetime



class CustomerUserForm(UserCreationForm):
    class Meta:
        model=User
        fields=['first_name','last_name','email','username']



class CustomerForm(forms.ModelForm):
    class Meta:
        model=Customer
        fields=['gender','profile_pic']

    
class CustomerUserUpdateForm(forms.ModelForm):
    class Meta:
        model=User
        fields=['first_name','last_name','email']


# class CustomerUpdateForm(forms.ModelForm):
#     class Meta:
#         model=Customer
#         fields=['gender','profile_pic']


# class CustomerUserForm2(forms.ModelForm):
#     class Meta:
#         model=User
#         fields=['first_name','last_name','email']


    
class CustomerRoomRegistration(forms.ModelForm):
    class Meta:
        model=HostelCustomer
        fields=['room','date_of_birth','age','check_in','duration','occupation','work_place','profession','caste','contact_number','guardian_name','guardian_relation','guardian_contact_number','emergency_contact_number','permanent_address','city','state','pincode']
        widgets={
            'date_of_birth':AdminDateWidget(),
            'check_in':AdminDateWidget(),
        }

    def clean(self):
        cleaned_data=super().clean()
        limited_age=16
        today=datetime.date.today()
        age=self.cleaned_data.get('age')
        birthlimityear=2005
        date_of_birth=self.cleaned_data.get('date_of_birth')
        if date_of_birth.year>birthlimityear:
            raise forms.ValidationError("Can't book a room,Enter proper date of birth")

        if age<limited_age:
            raise forms.ValidationError("Can't book a Room,Enter proper Age")

        check_in=self.cleaned_data.get('check_in')
        if check_in<today:
            raise forms.ValidationError("Can't book a room,Enter proper Date")

        contact_number=self.cleaned_data.get('contact_number')
        guardian_contact_number=self.cleaned_data.get('guardian_contact_number')
        emergency_contact_number=self.cleaned_data.get('emergency_contact_number')
        if contact_number==guardian_contact_number or contact_number==emergency_contact_number or guardian_contact_number==emergency_contact_number:
            raise forms.ValidationError("Enter different contact number")
        
        str_cn=str(contact_number)
        str_gcn=str(guardian_contact_number)
        str_ecn=str(emergency_contact_number)
        if len(str_cn)!=10 and len(str_gcn)!=10 and len(str_ecn)!=10:
            raise forms.ValidationError("Can't book a room,enter proper contact numbers")
        
            
                


class CustomerRoomCustomizationForm(forms.ModelForm):
    class Meta:
        model=CustomerRoomCustomization
        fields=['left','right','top','bottom','front','back']


class HostelCustomerUpdateform(forms.ModelForm):
    class Meta:
        model=HostelCustomer
        fields=['occupation','work_place','profession','caste','contact_number','guardian_name','guardian_relation','guardian_contact_number','emergency_contact_number','permanent_address','city','state','pincode']



class CustomerComplaintForm(forms.ModelForm):
    class Meta:
        model=CustomerComplaint
        fields=['complaint']
        