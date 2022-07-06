from turtle import textinput
from django.core import validators
from django import forms


class CustomerRegistration(forms.Form):
    name = forms.CharField(widget=forms.TextInput(attrs={'class':'inputn'}) , error_messages={'required':'Enter Your Name'})
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class':'inpute'}), error_messages={'required':'Enter Your Email'})
    contact = forms.CharField(widget=forms.NumberInput(attrs={'class':'inputc'}) ,error_messages={'required':'Enter a valid Phone Number'},min_length=10,max_length=10)
    age = forms.IntegerField(widget=forms.NumberInput(attrs={'class':'agec'}) ,error_messages={'required':'Enter Your Age'})
    # Gender = forms.EmailField(error_messages={'required':'Enter Your Email'})
    CHOICES = [('Male','Male'),('Female','Female')]
    gender=forms.CharField(label='Gender', widget=forms.RadioSelect(choices=CHOICES, attrs={'class':'gen'}))