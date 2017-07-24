from django import forms
from django.contrib.auth.models import User
from profiles.models import Profile


class FormForgotPasswordVerification(forms.Form):

    email = forms.EmailField(required=True)
    security_question = forms.ChoiceField(choices=Profile.DEFAULT_QUESTIONS, required=True)
    security_answer = forms.CharField(max_length=64, required=True)

    def is_valid_from_form(self):
        return super(FormForgotPasswordVerification, self).is_valid()

    def is_valid(self):
        valid = self.is_valid_from_form()
        data = self.cleaned_data
        user_exists = User.objects.filter(email=data['email']).exists()
        if not user_exists:
            valid = user_exists
            self.add_error(field="email", error="There isn't a registered account with this e-mail!")
        else:
            user = User.objects.get(email=data['email'])
            profile = Profile.objects.get(user=user)
            valid_security = profile.verify_security(
                security_question=data['security_question'],
                security_answer=data['security_answer']
            )
            if valid_security:
                valid = valid_security
            else:
                self.add_error(field=forms.ALL_FIELDS, error="Your security verification was invalid! Try again!")
        return valid


class FormForgotPasswordNew(forms.Form):

    email = forms.EmailField(required=True)
    new_password1 = forms.PasswordInput()
    new_password2 = forms.PasswordInput()

    def is_valid_from_form(self):
        return super(FormForgotPasswordNew, self).is_valid()

    def is_valid(self):
        valid = self.is_valid_from_form()
        data = self.data
        valid_password = data['new_password1'] == data['new_password2']
        user_exists = User.objects.filter(email=data['email']).exists()
        if not user_exists:
            valid = False
            self.add_error(field="email", error="There isn't a registered account with this e-mail!")
        if not valid_password:
            valid = False
            self.add_error(field=forms.ALL_FIELDS, error="The passwords don't match!")
        return valid


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
