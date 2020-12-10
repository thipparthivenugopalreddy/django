from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from . import forms
from django.http import HttpResponseRedirect

# Create your views here.
def base_view(r):
    return render(r,'indapp/base.html')

def home_view(r):
    # n=r.session['name']
    return render(r,'indapp/home.html')


@login_required
def python_view(r):
    return render(r,'indapp/python.html')

def java_view(r):
    return render(r,'indapp/java.html')

def logout_view(r):
    return render(r,'indapp/logout.html')

@login_required
def react_view(r):
    return render(r,'indapp/react.html')

def signup_view(r):
    f=forms.signup_form()
    if r.method=='POST':
        f=forms.signup_form(r.POST)
        if f.is_valid():
            user=f.save()
            user.set_password(user.password)
            user.save()
            r.session['name']=r.POST['username']
            return HttpResponseRedirect('accounts/login')
    return render(r,'indapp/singup.html',{'f':f})
