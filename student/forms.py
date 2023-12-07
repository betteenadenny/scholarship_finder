from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import StudentProfile

class StudentRegistrationForm(UserCreationForm):
    class Meta:
        model = StudentProfile  
        fields = ['username', 'first_name', 'last_name', 'email','type','category','annual_income','degree_type','major', 'password1', 'password2']

class StudentLoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)


class StudentUpdateForm(forms.ModelForm):
    class Meta:
        model = StudentProfile
        fields = ['type', 'category', 'annual_income', 'degree_type', 'major']

    def __init__(self, *args, **kwargs):
        super(StudentUpdateForm, self).__init__(*args, **kwargs)    
        self.fields['type'].widget.attrs['readonly'] = True
        self.fields['category'].widget.attrs['readonly'] = True
        self.fields['annual_income'].widget.attrs['readonly'] = True
        self.fields['degree_type'].widget.attrs['readonly'] = True
        self.fields['major'].widget.attrs['readonly'] = True

