from django.shortcuts import render
from django.shortcuts import render,redirect
from django.contrib.auth.models import AbstractUser,User,auth
from django.contrib import messages


# Create your views here.

def login(request):
    if request.method=='POST':
        username=request.POST['uname']
        password = request.POST['pwd1']
        user=auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('re')
        else:
            message.info(request,'login.html')


    return render(request,'login.html')


def register(request):
    if request.method == 'POST':

        username = request.POST['uname']


        password = request.POST.get('pwd',False)
        cpassword = request.POST.get('cpwd', False)
        if password == cpassword:
            if User.objects.filter(username=username).exists():
                messages.info(request, 'Username Taken')
                return redirect('register')

            else:
                user = User.objects.create_user(username=username,password=password)

                user.save();
                return redirect('login')
                print('User created')
        else:
            messages.info(request, 'Password not matched')
            return redirect('register')
        return redirect('/home')
    return render(request, 'register.html')


def home(request):
    return render(request,'home.html')
def llg(request):
    messages.info(request, 'Order Taken')

    return render(request,'fm.html')

def logout(request):
    auth.logout(request)
    return redirect('/home')

def re(request):
    return render(request,'llg.html')

def gg(request):


    return render(request,'gg.html')