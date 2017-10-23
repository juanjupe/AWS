from django import forms
from django.contrib.auth.forms import UserCreationForm
     
class UserForm(UserCreationForm):
	email = forms.EmailField()
	avatar = forms.ImageField()
