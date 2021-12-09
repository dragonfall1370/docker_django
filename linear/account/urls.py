from django.urls import path
from . import views

urlpatterns = [
    path('', views.hompage_without_login, name="homepage_without_login"), # our-domain.com/meetups   
    path('homepage', views.hompage, name="homepage"), # our-domain.com/meetups
    path('about', views.about, name="about"), # our-domain.com/meetups   
    path('login', views.loginpage, name="login"), # our-domain.com/meetups   
    path('register', views.registerpage, name="register"), # our-domain.com/meetups   
    path('user', views.users, name="users"), # our-domain.com/meetups   
    path('logout', views.logoutUser, name="logout") # our-domain.com/meetups   
    
]
