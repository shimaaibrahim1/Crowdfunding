from django import forms
from django.core.validators import RegexValidator

from .models import Account
from django.contrib.auth.forms import UserCreationForm


class UserRegisterationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    first_name = forms.CharField(required=True, max_length=30)
    last_name = forms.CharField(required=True, max_length=30)
    profile_picture = forms.ImageField(required=False)
    phone_regex = RegexValidator(regex=r'^[\+02]?(01)(0|1|2|5)([0-9]{8})$',
                                 message="Sorry, Egyptian Phone numbers are only allowed.")
    mobile = forms.CharField(validators=[phone_regex], max_length=14, required=False)  # validators should be a list

    # facebook = forms.CharField(required=False, max_length=200)
    # public_info = forms.CharField(required=False, widget=forms.Textarea)

    class Meta:
        model = Account
        fields = ['first_name', 'last_name', 'email', 'username', 'password1', 'password2', 'mobile', 'profile_picture']
        labels = {
            'email': 'Email',
            'first_name': 'First Name',
            'last_name': 'Last Name',
            'profile_picture': 'Profile Picture',
        }


class AccountUpdateForm(forms.ModelForm):
    class Meta:
        model = Account
        fields = ('email','username')

    def clean_email(self):
        if self.is_valid():
            email = self.cleaned_data['email']
            try:
                account = Account.objects.exclude(pk=self.instance.pk).get(email=email)
            except Account.DoesNotExist:
                return email
            raise forms.ValidationError('email "%s" is already in use' % account.email)

    def clean_username(self):
        if self.is_valid():
            username = self.cleaned_data['username']
            try:
                account = Account.objects.exclude(pk=self.instance.pk).get(username=username)
            except Account.DoesNotExist:
                return username
            raise forms.ValidationError('username "%s" is already in use' % account.username) 
