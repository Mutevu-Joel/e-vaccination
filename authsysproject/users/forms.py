from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from .models import Profile
from .models import vaccine
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
        model= vaccine
        fields = ['vaccine_id','mode_of_admission','vaccine_type','vaccine_quantity']

class ChildForm(forms.ModelForm):
    class Meta:
        model= Child
        fields = ['child_registration_no','Surname','Other_name','weight','height','DOB','parent_ID','phone_no','ward','Underlying_condition','immunization_type','immunization_dose_no','immunization_description']



