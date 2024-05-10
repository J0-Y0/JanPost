from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import (
    UserCreationForm,
    SetPasswordForm,
    PasswordResetForm,
)


class LoginForm(forms.Form):
    username = forms.CharField(
        max_length=40,
        required=True,
        widget=forms.TextInput(
            attrs={"class": "form-control", "placeholder": "Username"}
        ),
    )
    password = forms.CharField(
        max_length=40,
        required=True,
        widget=forms.PasswordInput(
            attrs={"class": "form-control ", "placeholder": "password"}
        ),
    )


class SignupForm(UserCreationForm):
    password1 = forms.CharField(
        label="Password",
        required=True,
        widget=forms.PasswordInput(
            attrs={"class": "form-control", "placeholder": "password"}
        ),
    )
    password2 = forms.CharField(
        label="Confirm Password",
        required=True,
        widget=forms.PasswordInput(
            attrs={"class": "form-control", "placeholder": "confirm"}
        ),
    )

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")
        widgets = {
            "password1": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Password",
                    "type": "password",
                }
            ),
            "username": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "UserName"}
            ),
            "password2": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "re-type the Password",
                    "type": "password",
                }
            ),
            "email": forms.EmailInput(
                attrs={
                    "required": "True",
                    "class": "form-control",
                    "placeholder": "Email",
                    "type": "email",
                }
            ),
        }

        def clean_password2(self):
            password1 = self.cleaned_data["password1"]
            password2 = self.cleaned_data["password2"]
            if password1 and password2 and password1 != password2:
                raise forms.ValidationError("Passwords don't match")
            return password2

        def clean_username(self):
            username = self.cleaned_data["username"]
            if User.objects.filter(username=username).exists():
                raise forms.ValidationError("Username already exists")
            return username

        def clean_email(self):
            email = self.cleaned_data["email"]
            if User.objects.filter(email=email).exists():
                raise forms.ValidationError("Email already taken")
            return email


class PwdResetRequestForm(PasswordResetForm):
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={"class": "form-control", "placeholder": "Email"})
    )

    def clean_email(self):
        email = self.cleaned_data["email"]
        if not User.objects.filter(email=email).exists():
            raise forms.ValidationError("Sorry, we could not find your account.")
        return email


class PwdResetForm(SetPasswordForm):
    new_password1 = forms.CharField(
        label="New password",
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control mb-3",
                "placeholder": "New Password",
                "id": "form-newpass",
            }
        ),
    )
    new_password2 = forms.CharField(
        label="Repeat password",
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control mb-3",
                "placeholder": "New Password",
                "id": "form-new-pass2",
            }
        ),
    )

    def clean_new_password2(self):
        password1 = self.cleaned_data["new_password1"]
        password2 = self.cleaned_data["new_password2"]
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords don't match")
        return password2
