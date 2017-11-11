from django import forms
from .models import Images, Comments
from django.contrib.auth.forms import (
    AuthenticationForm, 
    UserCreationForm
    )
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm



class CommentsForm(forms.ModelForm):
    image_name = forms.ModelChoiceField(queryset=Images.objects.none(), required=False, widget=forms.HiddenInput())
    comment = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'name' : 'comment'}))
#   comment_dt = forms.DateTimeField()
    
    class Meta:
        model = Comments
        fields = ('image_name', 'comment',)       
      
    def __init__(self, *args, **kwargs):
        image = kwargs.get('image_name')
        super(CommentsForm, self).__init__(*args, **kwargs)
        self.fields['image_name'] = Images.objects.filter(image_name=image)     
     
        
class LoginForm(AuthenticationForm):
    username = forms.CharField(label="Username", max_length=30, widget=forms.TextInput(attrs={'class':'form-control', 'name' : 'username'}))
    password = forms.CharField(label="Password", max_length=30, widget=forms.TextInput(attrs={'class':'form-control', 'name' : 'password'}))


class RegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)
        
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')       
