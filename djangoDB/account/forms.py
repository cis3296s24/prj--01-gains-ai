from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.forms.widgets import PasswordInput, TextInput
from .models import FitnessRecord
from .models import Checkin

class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2', 'first_name', 'last_name']
    
class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=TextInput())
    password = forms.CharField(widget=PasswordInput())


class FitnessRecordForm(forms.ModelForm):
    class Meta:
        model = FitnessRecord
        fields = '__all__'

class CheckinForm(forms.ModelForm):
    class Meta:
        model = Checkin
        fields = ['date']