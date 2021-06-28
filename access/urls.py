from django.contrib import admin
from django.urls import path,include
from . import views
urlpatterns = [
    path('',views.homepage,name='home'),
   
    path('login/',views.login_page,name='login'),
    path('signup/',views.signup_page,name='signup'),
     path('logout/',views.logout_page,name='logout'),
    path('forgot/',views.forget_pass,name='forget'),
    path('blog/phishing/',views.phis,name='kali'),
    path('blog/kali-install/',views.kali,name='install'),
    path('blog/tool-x/',views.tool,name='tool-x'),
    path('blog/',views.blog,name='tool-x'),
   

    
]
