from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
class UserRegisterationForm(forms.Form):
    form_register_username = forms.CharField(widget=forms.TextInput(attrs={"class" : "form-control" , "placeholder" : "your username"}))
    form_register_email = forms.EmailField(widget=forms.EmailInput(attrs={"class" : "form-control" , "placeholder" : "your email address"}))
    form_register_password1 = forms.CharField(widget=forms.PasswordInput(attrs={"class" : "form-control" , 'placeholder' : "your password"})) #widgets apply new feutures on our forms
    form_register_password2 = forms.CharField(label='confirm password',widget=forms.PasswordInput(attrs={"class" : "form-control" , 'placeholder' : "your password again"})) #widgets apply new feutures on our forms

    #                                                        ^ -> attrs are HTML attributes


    def clean_form_email(self): #clean_ is sabet , form_email is the field |  this function will be ran when is_valid() is ran
        email = self.cleaned_data['form_register_email'] #get that email from the form
        #user = User.objects.filter(form_email = email)
        user = User.objects.filter(email=email).exists() #exists only returns True or False not its data like the above code , it helps performance
        #                           ^-> this email is the email-field in User built in  model
        if user : # if it was not ok it returns the user | if we dont use exists() the whole data will be terminated but now with exists it only returns True of False
            raise ValidationError('this email already exists') # now validation proccess stops
        return email #we return the email to be passed through other codes in app like is_valid()



    #username has its own unique value is dosn't need clean() but it returns error

    def clean_form_username(self):
        username = self.cleaned_data['form_register_username']
        user = User.objects.filter(username=username).exists() #if user with that username exists it fills , if not , it fills it with None

        if user : #if user was True : | we check that if the user with the given username exists
            raise ValidationError('this username already exists') #Now validation process stops
        return username # pas mide username ro be marahel badi mesl is_valid()


    def clean(self): #it overrides the clean function  | its good to know that previous cleans are also overwritten to this clean function
        cd = super().clean() # super here calls the clean method from its parent class means form (UserRegistreationForm)
        p1 = cd.get("form_register_password1")
        p2 = cd.get('form_register_password2')

        if p1 and p2 and p1 != p2:
            raise ValidationError("passwords must match") #now validation process stops


class UserLoginForm(forms.Form):
    form_login_username = forms.CharField(widget=forms.TextInput(attrs={"class" : "form-control" , "placeholder" : "your username"}))
    form_login_password = forms.CharField(widget=forms.PasswordInput(attrs={"class" : "form-control" , 'placeholder' : "your password"}))
