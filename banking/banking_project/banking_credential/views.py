
# Create your views here.
from urllib import request

from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect, HttpResponse

from django.shortcuts import render, redirect
from django.template import loader


def registration(request):
    if request.method=='POST':
        username = request.POST['username']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        password = request.POST['password']
        confirm_password= request.POST['cpassword']
        if password==confirm_password:
            if User.objects.filter(username=username).exists():
                messages.info(request,"Username already taken")
                return redirect("registration")
            elif User.objects.filter(email=email).exists():
                messages.info(request,"email already taken")
                return redirect("registration")
            else:
                user = User.objects.create_user(username=username,first_name=first_name,last_name=last_name,email=email,password=password)
                user.save()
                return redirect("login")

        else:
            messages.info(request,"password not matching")
            return redirect("registration")
        return redirect("/")
    return render(request,"registration.html")

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user=auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect("/")
        else:
            messages.info(request,"invalid credential")
            return redirect("login")
    return render(request, "login.html")
def new_form(request):
    return render(request, "new_form.html")

#def msgAlert():
#    template=loader.get_template('template.html')
#    return HttpResponse(render(request))

def logout(request):
    auth.logout(request)
    return redirect('/')