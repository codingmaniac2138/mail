from .models import *
from django import forms
# lib files for sign up form
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


# # lib files
# class country_form(forms.ModelForm):
#     class Meta:
#         model=country
#         fields= ['country_drop','states_drop_ind','states_drop_usa',]

# class for sign up form
class MyForm(UserCreationForm):
    email = forms.EmailField(required=True, label='KDEMAIL')
    username = forms.CharField(required=True, label='KDuser')
    password1 = forms.PasswordInput()
    password2 = forms.PasswordInput()
    # firstname=forms.CharField(required=True)
    # lastname=forms.CharField(required=True)
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')

    # def save(self, commit=True):
    #     user=super(MyForm,self).save(commit=False)
    #     user.email=self.cleaned_data['email']
    #     # user.firstname=self.cleaned_data['firstname']
    #     # user.lastname=self.cleaned_data['lastname']
    #
    #     if commit:
    #         user.save()
    #     return user

    def clean_email(self):
        email = self.cleaned_data["email"]
        try:
            User._default_manager.get(email=email)
        except User.DoesNotExist:
            return email
        raise forms.ValidationError('duplicate email')

    # modify save() method so that we can set user.is_active to False when we first create our user
    def save(self, commit=True):
        user = super(MyForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.is_active = False  # not active until he opens activation link
            user.save()

        return user


class edit_profile_form(forms.ModelForm):
    class Meta:
        model = edit_profile
        widgets = {
            'consultant_name': forms.TextInput(),
            'technology': forms.TextInput(attrs={'placeholder': "Enter comma separated passwords"}),
            'job_location': forms.TextInput(attrs={'placeholder': "Enter comma separated id's"}),
            'requested_email': forms.EmailInput(attrs={'placeholder': "Enter emailfield"}),
        }
        fields = ('consultant_name', 'technology', 'job_location','requested_email',)
