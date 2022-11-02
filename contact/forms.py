from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import Contact


class ContactForm(ModelForm):
	class Meta:
		model = Contact
		fields = '__all__'

class CreateUserForm(UserCreationForm):
	class Meta:
		model = User
		fields =  '__all__'
