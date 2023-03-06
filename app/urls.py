from django.urls import path
from . import views

app_name = 'app'
urlpatterns = [
    path("", views.home, name='home'),
    path("app/addprofile/", views.addprofile, name='addprofile'),
    path("login/", views.login, name='login'),
    path("login/posts/", views.posts, name='posts')
]