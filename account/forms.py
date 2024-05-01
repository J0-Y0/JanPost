from django import forms

class LoginForm(forms.Form):
    username = forms.CharField(max_length=40, required=True,
                               widget=forms.TextInput(attrs={'class':'form-control','placeholder':"Username"}))
    password = forms.CharField(max_length=40, required=True,
                               widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'password'}))
                               

