from django.shortcuts import render, redirect
from django.views import generic
from django.utils import timezone
from .models import Album, Images, Comments
from .forms import LoginForm, CommentsForm, RegistrationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm


data = '..created this website to showcase my technical skills and ability to design a website using Django framework.'


def index(request):
    context = {'data':data}
    return render(request, 'photos/home.html', context)

   
def home(request, home):
    albums = Album.objects.all()
    context = {'albums':albums,
               'data':data
              }
    return render(request, 'photos/home.html', context)


class albumsView(generic.ListView):
    template_name = 'photos/albums.html'
    context_object_name = 'albums'
    albums = Album.objects.all()
    
    def get_queryset(self):
        return Album.objects.all()


def contact(request, contact):
    context = {"email" : "Email : maneesha.vinayak@gmail.com"}
    return render(request, 'photos/contact.html', context)


def register(request):
    if request.method=='POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            reg = form.save(commit=False)
            reg.save()
            context = {'success':'Successfully Registered. Login to continue', 'data':data}
            return render(request, 'photos/home.html', context)
        else:
            context = {'form':form}
            return render(request, 'photos/register.html', context)
    else:
        form = RegistrationForm()
        context = {'form':form, 'data':data}
        return render(request, 'photos/register.html', context)
        

def random(request, album_name):    
    images = Images.objects.filter(album_name=album_name)
    comments = Comments.objects.all()
        
    if request.method == 'POST': 
        if 'Likes' in request.POST: 
            input_image_name = request.POST.get('image_name')
            image = Images.objects.get(image_name=input_image_name)
            image.like_cntr += 1
            image.save()
        elif 'Comment' in request.POST:
            pass
             
    context = {'album_name':album_name, 'images' :images, 'comments':comments}
    return render(request, 'photos/random.html', context)
