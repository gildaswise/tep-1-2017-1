from django import forms

class FormRegisterUser(forms.Form):
    name = forms.CharField(required=True)
    email = forms.EmailField(required=True)
    password = forms.PasswordInput()
    phone = forms.CharField(required=True)
    business = forms.CharField(required=True)
