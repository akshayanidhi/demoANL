from urllib import request

from django.http import HttpResponse
# Create your views here.
from django.shortcuts import render, redirect
# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render

def operations(request):
    #obj=place.objects.all()
    #team_obj=team.objects.all()
    #name = "friends"
    #return render(request, "index1.html",{'obj' :name,})
    #return render(request, "formpage.html")
    return render(request,"index1.html")


#def Home(request):
   # return render(request,"index1.html")

#def About(request):
 #  return render(request, "About1.html")
