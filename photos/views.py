from django.views import generic
from django.shortcuts import render, redirect
from django.utils import timezone
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404
from .models import Album, Images, Comments
from django.db.models import OuterRef, Subquery
from .forms import ImagesForm, LoginForm, CommentsForm
from django.views.generic import TemplateView
from django.contrib.auth.decorators import login_required
from django.contrib.auth import (
    authenticate, logout
    )


class IndexView(generic.ListView):
    template_name = 'photos/home.html'
    context_object_name = 'albums'
    
    def get_queryset(self):   
        return Album.objects.all()

    
   
def home(request, home):
    albums = Album.objects.all()
    context = {'albums' : albums}
    return render(request, 'photos/home.html', context)
  

def contact(request, about):
    context = {"html_var" : "Django"}
    return render(request, 'photos/contact.html', context)


''''
class RandomView(TemplateView):
    template_name = 'photos/random.html'
     
    def get(self, request, album_name):
        images = Images.objects.filter(album_name=album_name)
        comments = Comments.objects.all()
    
        context = {'album_name':album_name, 'images' : images, 'comments' :comments}
        return render(request, 'photos/random.html', context)         
     
    def post(self, request, album_name):
        form = CommentsForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.image_name = Images.objects.filter(image_name = form.cleaned_data['image_name'])
            comment.save()
        else:
            print(form.errors)
            return render(request, 'photos/random.html', {'form': form} )
        
        
#         else:
#             images = Images.objects.filter(album_name=album_name)
#            context = {'album_name':album_name, 'images' : images }
#           return render(request, self.template_name, context)

         
'''        


def random(request, album_name):
        
    images = Images.objects.filter(album_name=album_name)
    comments = Comments.objects.all()
    print(comments)
    
    if request.method == 'POST': 
        if 'Likes' in request.POST: 
            input_image_name = request.POST.get('image_name')
#        image_name_input = request.POST.get('image_name')
            image = Images.objects.get(image_name=input_image_name)
            image.like_cntr += 1
            image.save()
        elif 'Comment' in request.POST:
            pass
             
    context = {'album_name':album_name, 'images' : images, 'comments' :comments}
    return render(request, 'photos/random.html', context)
    
    
    
