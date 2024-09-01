from django import forms

class UserRegistrationForm(forms.Form):
    register_form_username = forms.CharField()
    register_form_password = forms.CharField()
    register_form_email = forms.EmailField()


class UserLoginForm(forms.Form):
    login_form_username = forms.CharField()
    login_form_password = forms.CharField()


