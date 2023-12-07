from django import forms
from .models import ExternalOrganization
from django.contrib.auth import get_user_model

class OrganizationRegistrationForm(forms.ModelForm):
    password1 = forms.CharField(widget=forms.PasswordInput)
    password2 = forms.CharField(widget=forms.PasswordInput)
    user_type = forms.CharField(widget=forms.HiddenInput(), initial=ExternalOrganization)
    class Meta:
        model = ExternalOrganization
        fields = ['username', 'name', 'email', 'website', 'file_title', 'file', 'password1', 'password2']

    def save(self, commit=True):
        user = get_user_model().objects.create(
            username=self.cleaned_data['username'],
            email=self.cleaned_data['email'],
        )

        # Set the password using set_password method
        user.set_password(self.cleaned_data['password1'])

        if commit:
            user.save()

        # Create the ExternalOrganization instance and associate it with the User
        organization = ExternalOrganization.objects.create(
            account = user,
            username=self.cleaned_data['username'],
            email=self.cleaned_data['email'],
            name=self.cleaned_data['name'],
            website=self.cleaned_data['website'],
            file_title=self.cleaned_data['file_title'],
            file=self.cleaned_data['file']
        )

        return user

class OrganizationLoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)
