from django import forms
from django.contrib.auth.models import User



class UserForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ('username', 'password', 'date_joined' )
        widgets = {
            'password' : forms.PasswordInput(attrs={'class': 'input', 'placeholder': 'votre Mot de passe svp'}),
            'date_joined' : forms.TextInput(attrs={'id': 'disp'})

        }