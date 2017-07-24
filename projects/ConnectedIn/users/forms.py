from django import forms
from django.contrib.auth.models import User
from profiles.models import Profile


class FormRegisterUser(forms.Form):

    name = forms.CharField(max_length=64, required=True)
    email = forms.EmailField(required=True)
    password = forms.PasswordInput()
    phone = forms.CharField(max_length=12, required=True)
    business = forms.CharField(max_length=32, required=True)
    security_question = forms.ChoiceField(choices=Profile.DEFAULT_QUESTIONS, required=True)
    security_answer = forms.CharField(max_length=64, required=True)

    def is_valid_from_form(self):
        return super(FormRegisterUser, self).is_valid()

    def is_valid(self):
        valid = self.is_valid_from_form()
        user_exists = User.objects.filter(email=self.cleaned_data['email']).exists()
        if user_exists:
            valid = not user_exists
            self.add_error(field="email", error="There's an account with that e-mail already!")
        return valid

    def clean(self):
        super(FormRegisterUser, self).clean()
