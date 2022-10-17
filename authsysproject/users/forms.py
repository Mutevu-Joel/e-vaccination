from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from .models import Immunization, Profile
from .models import Vaccine
from .models import Child


class CreateUserForm(UserCreationForm):
    email=forms.EmailField()

    class Meta:
        model = User
        fields = ['username','email', 'password1', 'password2']

class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email']

class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['phone', 'address', 'image']

class VaccineForm(forms.ModelForm):
    class Meta:
        model= Vaccine
        fields = ['vaccine_id','mode_of_admission','vaccine_type','vaccine_quantity']
        
class ImmunizationForm(forms.ModelForm):
    class Meta:
        model= Immunization
        fields = ['vaccine_id','vaccine_type','immunization_description']

class DateInput(forms.DateInput):
    input_type = 'date'
    
class ChildForm(forms.ModelForm):
    class Meta:
        model= Child
        fields = ['child_registration_no','Surname','Other_name','weight','sex','height','DOB','parent_ID','phone_no','ward','Underlying_condition','vaccine_id','vaccine_type','immunized_at','immunization_description']
        widgets = {
            'immunized_at':DateInput(),
            'DOB':DateInput(),
        }




