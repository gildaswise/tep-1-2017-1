from django import forms
from django.contrib.auth.models import User


class FormRegisterUser(forms.Form):
    name = forms.CharField(required=True)
    email = forms.EmailField(required=True)
    password = forms.PasswordInput()
    phone = forms.CharField(required=True)
    business = forms.CharField(required=True)

    def is_valid_from_form(self):
        return super(FormRegisterUser, self).is_valid()

    def is_valid(self):
        valid = self.is_valid_from_form()
        user_exists = User.objects.filter(email=self.cleaned_data['email']).exists()
        if user_exists:
            valid = not user_exists
            self.add_error(field="email", error="There's an account with that e-mail already!")
        return valid
