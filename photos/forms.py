from django import forms
from .models import Images, Comments
from django.contrib.auth.forms import AuthenticationForm


class ImagesForm(forms.ModelForm):
    album_name = forms.CharField()
    description = forms.CharField(required=False)
    
    class Meta:
        model = Images
        fields = ('album_name', 'description',)
        

class CommentsForm(forms.ModelForm):
    image_name = forms.CharField(required=False,widget=forms.HiddenInput())
    comment = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'name' : 'comment'}))
 #   comment_dt = forms.DateTimeField()
    
    class Meta:
        model = Comments
        fields = ('image_name', 'comment',)   
    
#    def __init__(self, *args, **kwargs):
#        image_name=kwargs.pop('image_name','')
#        super(CommentsForm, self).__init__(*args, **kwargs)
#        self.fields['image_name']=forms.ModelChoiceField(queryset=Images.objects.filter(image_name=image_name))
         
    
        
class LoginForm(AuthenticationForm):
    username = forms.CharField(label="Username", max_length=30, widget=forms.TextInput(attrs={'class':'form-control', 'name' : 'username'}))
    password = forms.CharField(label="Password", max_length=30, widget=forms.TextInput(attrs={'class':'form-control', 'name' : 'password'}))
    
    
    