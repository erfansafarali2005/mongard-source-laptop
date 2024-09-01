from django import forms
from .models import Todo

class TodoCreateForm(forms.Form): # a class which declears your form fields it must inherits from forms.Form
    form_title = forms.CharField()  #these field's names are the name of our field in html that are sent into cleaned_Data
    form_body = forms.CharField()

class TodoUpdateForm(forms.ModelForm):#model form is a method that declears a form fields from your model
    class Meta: #meta class is a kind of a class that edits the main parent class -> watch meta class tutorials on mongard.ir
        model = Todo #the model that it inherits from
        fields = ('title' , 'body') #field that it should inherits
       #fields = (,) -> this takes all fields from the model