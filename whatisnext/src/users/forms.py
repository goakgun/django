from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

from .models import User

class UserForm(forms.ModelForm):
    class Meta:
        model=User
        widgets = {
        'password': forms.PasswordInput(),
        }
        
class MyRegisterationForm(UserCreationForm):
    email=forms.EmailField(required=True)
    class Meta:
        model=User
        fields=('username','email','password1','password2')
    def save(self,commit=True):
        user=super(UserCreationForm,self).save(commit=False)
        user.email=self.cleaned_data['email']
        if commit:
            user.save()
        return user
        
    
