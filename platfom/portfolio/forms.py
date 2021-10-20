from django.forms import fields
from portfolio.models import Profile, Project

from django import forms 
from django.core.exceptions import ValidationError


class ProfileForm(forms.ModelForm):

    class Meta:
        model = Profile
        fields = ('name', 'last_name', 'email', 'photo', 'phone')

    
class ProjectForm(forms.ModelForm):
    class Meta:
        model  = Project
        fields = ( 'title', 'description', 'photo', 'category')

            