from django.shortcuts import render
from .forms import UserForm,LoginForm
from app.models import Post, Comment


# Create your views here.

def home(request):
    return render(request, 'app/home.html')

def addprofile(request):
    form = UserForm()
    return render(request,'app/profile.html',{'form': form})

def login(request):
    form = UserForm()
    return render(request,'app/login.html',{'form': LoginForm})

def posts(request):
    post_list= Post.objects.all()
    comment_list=Comment.objects.all()
    return render(request,'app/posts.html',{'post_list': post_list,'comment_list': comment_list})