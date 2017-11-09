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
    image_name = forms.ModelChoiceField(queryset=Images.objects.none(), required=False, widget=forms.HiddenInput())
    comment = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'name' : 'comment'}))
#   comment_dt = forms.DateTimeField()
    
    class Meta:
        model = Comments
        fields = ('image_name', 'comment',)       
        
    def __init__(self, image_name, *args, **kwargs):
        image = kwargs.get('image_name')
        super(CommentsForm, self).__init__(*args, **kwargs)
        self.fields['image_name'] = Images.objects.filter(image_name=image)     
 
  
'''            
    def save(self, commit=True):
        instance = super(CommentsForm, self).save(commit=False)
#        instance.comment = self.cleaned_data['comment']
#        instance.fields['image_name'].queryset = Images.objects.filter(image_name=request.image_name)
#        instance.image_name
#        image_name_input = self.cleaned_data['image_name']
#        image_name_fm = image_name_input.replace("'", '')
#        image = Images.objects.get(image_name=image_name_fm)
#        instance.image_name = image.image_name
        if commit:
            instance.save()
        return instance
 '''            
    
        
class LoginForm(AuthenticationForm):
    username = forms.CharField(label="Username", max_length=30, widget=forms.TextInput(attrs={'class':'form-control', 'name' : 'username'}))
    password = forms.CharField(label="Password", max_length=30, widget=forms.TextInput(attrs={'class':'form-control', 'name' : 'password'}))
    
    
    
