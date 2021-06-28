from django.shortcuts import render,redirect
from .forms import *
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required


def login_page(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        if request.method=='POST':
            check=request.POST.get('type')
            if check=='email':
                user=User.objects.get(email=request.POST.get('email'))
                username=user.username
            else:
                username=request.POST.get('email')
            print(username)
            password=request.POST.get('password')
            user=authenticate(request,username=username,password=password)
            if user is not None:
                login(request,user)
                return redirect('home')
            else:
                print('wrong;')
                messages.error(request, 'Username or Password is Incorrect!')
                
        return render(request,'login.html',context={})
def logout_page(request):
    logout(request)
    return redirect('login')
    
    
    return render(request,'login.html')
def signup_page(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        form=signupform()
        if request.method=='POST':
            form=signupform(request.POST)
            if form.is_valid():
                    email=request.POST.get('email')
                    if User.objects.filter(email=email):
                       print(User.objects.filter(email=email))
                       messages.error(request, 'Email is already Taken!')
                       print('Email is already Taken!')
                    else:
                        form.save()
                        username=request.POST.get('username')
                        password=request.POST.get('password1')
                        user=authenticate(request,user=username,password=password)
                        print('failed!')
                        if user is not None:
                            login(request,user)
                        return redirect('home')

        context={'signupform':form}
        return render(request,'signup.html',context)
def forget_pass(request):
    return render(request,'frg.html')
@login_required(login_url='login')
def homepage(request):
    return render(request,'index h.html')
@login_required(login_url='login')
def blog(request):
    return render(request,'blog.html')
@login_required(login_url='login')
def kali(request):
    return render(request,'ins-kali.html')

@login_required(login_url='login')
def phis(request):
    return render(request,'phi-blo.html')

@login_required(login_url='login')
def tool(request):
    return render(request,'tool-x.html')
# Create your views here.
