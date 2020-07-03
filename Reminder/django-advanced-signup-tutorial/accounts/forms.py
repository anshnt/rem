from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=100, help_text='Last Name')
    last_name = forms.CharField(max_length=100, help_text='Last Name')
    username = forms.CharField(max_length=100, help_text='Unique')
    phone_no = forms.IntegerField()
    email = forms.EmailField(max_length=150, help_text='Email')
    gst = forms.IntegerField()
    aadhar = forms.IntegerField()
    pan = forms.IntegerField()

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username', 'phone_no', 'email', 'gst', 'aadhar', 'pan', 'password1',
                  'password2')
