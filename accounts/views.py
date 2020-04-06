from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.models import User,auth
# Create your views here.

def login(request):
    if request.method=='POST':
        uname=request.POST['luname']
        upass=request.POST['lpass']
        user=auth.authenticate(username=uname,password=upass)
        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else:
            messages.info(request,'invalid credetials')
            return redirect('login')    
    else:
        return render(request,'login.html')

def register(request):
    if request.method == 'POST':
        fname=request.POST['fname']
        lname=request.POST['lname']
        uname=request.POST['uname']
        email=request.POST['email']
        pass1=request.POST['pass1']
        pass2=request.POST['pass2']
        if pass1==pass2:
            if User.objects.filter(username=uname).exists():
                messages.info(request,'username taken')
                return redirect('register')
            elif User.objects.filter(email=email).exists():    
                messages.info(request,'email exist')
                return redirect('register')
            else:    
                user= User.objects.create_user(username=uname,password=pass1,email=email,first_name=fname,last_name=lname)
                user.save()
                return redirect('login')
        else:
            messages.info(request,'password not matching...')  
            return redirect('register')      
        return redirect('/')
    else:
        return render(request,'register.html')


def logout(request):
    auth.logout(request)
    return redirect('/')        