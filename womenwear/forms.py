from cProfile import label
import email
from pyexpat import model
from select import select
from tkinter import Label, Widget
from attr import attrs, fields
from django import forms
from django.contrib.auth.forms import UserCreationForm , AuthenticationForm , UsernameField, PasswordChangeForm,PasswordResetForm,SetPasswordForm
from django.contrib.auth.models import User
from django.contrib.auth import password_validation
from pkg_resources import require
from razorpay import Customer
from womenwear.models import customer


class customerRegistraionForm(UserCreationForm):
    password1 = forms.CharField(label='Password' , widget=forms.PasswordInput(attrs={'class':'form-control'}))
    password2 = forms.CharField(label='Confirm Password(again)' , widget=forms.PasswordInput(attrs={'class':'form-control'}))
    email = forms.CharField(required=True,widget=forms.EmailInput(attrs={'class':'form-control'}))
    
class meta:
    model = User
    fields = ['username','email','password1','password2']
    labels = {'email':'Email'}
    Widget = {'username': forms.TextInput(attrs={'class':'form-control'})}


class LoginForm(AuthenticationForm):
    username = UsernameField(widget=forms.TextInput(attrs={'autofocus':True}))
    password = forms.CharField(label=("Password"),strip=False, widget=forms.PasswordInput(attrs={'autocomplete':'current-password'}))

class MyPasswordChangeForm(PasswordChangeForm):
    old_password = forms.CharField(label=("Old Password:"),strip=False,widget=forms.PasswordInput(attrs={'autocomplete':'current-password','autofocus':True}))
    new_password1 = forms.CharField(label=("New Password:"),strip=False,widget=forms.PasswordInput(attrs={'autocomplete':'new-password'}),help_text= password_validation.password_validators_help_text_html())
    new_password2 = forms.CharField(label=("Confirm New Password:"),strip=False,widget=forms.PasswordInput(attrs={'autocomplete':'new-password'}))


class MypasswordResetForm(PasswordResetForm):
    email = forms.EmailField(label=('Email-id'),max_length=250,widget=forms.EmailInput(attrs={'autocomplete':'email'}))

class MySetPasswordForm(SetPasswordForm):
    new_password1 = forms.CharField(label=("New Password:"),strip=False,widget=forms.PasswordInput(attrs={'autocomplete':'new-password'}),help_text= password_validation.password_validators_help_text_html())
    new_password2 = forms.CharField(label=("Confirm New Password:"),strip=False,widget=forms.PasswordInput(attrs={'autocomplete':'new-password'}))

    
class CustomerProfileForm(forms.ModelForm):
    class  Meta:
        model = customer
        fields = ['name','address','Mobile_no','locality','city','state','zipcode','country']
        widgets ={'name':forms.TextInput(attrs={'class':'form-control'}),'Mobile_no':forms.TextInput(attrs={'class':'form-control'}),'address':forms.TextInput(attrs={'class':'form-control'}),'locality':forms.TextInput(attrs={'class':'form-control'}),'city':forms.TextInput(attrs={'class':'form-control'}),'state':forms.Select(attrs={'class':'form-control'}),'zipcode':forms.NumberInput(attrs={'class':'form-control'}),'country':forms.Select(attrs={'class':'form-control'})}
