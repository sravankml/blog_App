from django.shortcuts import render,get_object_or_404
from django.contrib.auth.models import User
from django.contrib.contenttypes.models import ContentType
# Create your views here.
from django.contrib.auth import (
    authenticate,
    get_user_model,
    login,
    logout,

    )
from django.shortcuts import render, redirect
from django.http import HttpResponse,HttpResponseRedirect,Http404

from .forms import UserLoginForm,UserRegisterForm,EditUserProfile
from django.contrib.auth.forms  import UserChangeForm

def login_view(request):
    title= "login"
    form = UserLoginForm(request.POST or None)
    if form.is_valid():
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get('password')
        user = authenticate(username=username, password=password)
        login(request, user)
        return redirect('/')
    return render(request, "form_login.html", {"form":form, "title": title})
def register_view(request):
    print(request.user.is_authenticated())
    next = request.GET.get('next')
    title = "Register"
    form = UserRegisterForm(request.POST or None)
    if form.is_valid():
        user = form.save(commit=False)
        password = form.cleaned_data.get('password')
        user.set_password(password)
        user.is_staff=True
        user.save()
        new_user = authenticate(username=user.username, password=password)
        login(request, new_user)
        return redirect('/front')
    context = {
        "form": form,
        "title": title
    }
    return render(request, "form_login.html", context)
def logout_view(request):
    logout(request)
    return redirect("/")
def profileedit(request):  
    pass
    if request.method == 'POST':
        form = EditUserProfile(request.POST,instance= request.user)
        if form.is_valid():
            form.save()
            return redirect("/profile")
    else:
        form = EditUserProfile(instance= request.user)
        context={
        'forms':form
        }
        
    return render(request,"edit_profile.html",context)