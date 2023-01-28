from django import forms
from django.forms import ModelForm
from .models import Message


class MessageForm(ModelForm):
    body=forms.CharField(widget=forms.Textarea(attrs={"class":"forms","rows":3,"placeHolder":"type message here"}))
    class Meta:
        model=Message
        fields=["body",]

class LoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={"class": "form-control"}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={"class": "form-control"}))
