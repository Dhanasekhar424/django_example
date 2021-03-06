from django.shortcuts import render
from login_app.forms import UserForm,UserProfileInfoForm

from django.contrib.auth import authenticate,login,logout
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required

# Create your views here.
def index(request):
    thanks={'import_text': 'this login app' }
    return render(request,'login_app/index.html',context=thanks)

def user_login(request):
    #return render(request,'login_app/login.html')
    if request.method == 'POST':

        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username,password=password)
        if user:
            if user.is_active:
                login(request,user)
                return HttpResponseRedirect(reverse('login_app:index'))
            else:
                return HttpResponseRedirect("account not active.")
        else:
            print("someone tried to login and failed.")
            print("username{} and password{}".format(username,password))
            return HttpResponseRedirect("invalid login details")
    else:
        return render(request,"login_app/login.html")
@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))

@login_required
def special(request):
    return HttpResponseRedirect("are you loged in.")

        
        


def register(request):
    return render(request,'login_app/register.html')

def base(request):
    return render(request,'login_app/base.html')

def link(request):
    return render(request,'login_app/link.html')


def register(request):
    registered=False
    if request.method=='POST':
        user_form=UserForm(data=request.POST)
        profile_form=UserProfileInfoForm(data=request.POST)
        if user_form.is_valid() and profile_form.is_valid():
            user=user_form.save()
            user.set_password(user.password)
            user.save()
            profile=profile_form.save(commit=False)
            profile.user=user

            if 'profile_pic' in request.FILES:
                profile.profile_pic=request.FILES['profile_pic']
            profile.save()
            registered=True
        else:
            print(user_form.errors,profile_form.errors)
    else:
        user_form=UserForm()
        profile_form=UserProfileInfoForm()

    return render(request,'login_app/register.html',{'user_form':user_form,'profile_form':profile_form,'registered':registered})


                  

