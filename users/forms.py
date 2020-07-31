from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile

class UserRegisterForm(UserCreationForm):
    email=forms.EmailField(required=True)

    class Meta:
        model=User
        fields = ['username','email','password1','password2']
    
#https://www.geeksforgeeks.org/django-modelform-create-form-from-models/ Reference for model fields
# Modelforms allows us to create a form closely related to our model.
class UserUpdateForm(forms.ModelForm):
    email=forms.EmailField()
    class Meta:
        model=User
        fields = ['username','email']       #The fields can be fields=__all__ but django documentation recommends this method

class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model=Profile
        fields=['image']


