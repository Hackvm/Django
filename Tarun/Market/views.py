from django.shortcuts import render
from .models import Fruits,Vegitables,lentils,Rice,Grocessory,UserFruits
from django.http import HttpResponseRedirect
from django.urls import reverse
# Create your views here.
def index(request):
    return render(request,"Market/index.html",{
        "fruits" : Fruits.objects.all(),
        "vegitable" : Vegitables.objects.all(),
        "lentil" : lentils.objects.all(),
        "rice" : Rice.objects.all(),
        "grocessory" :Grocessory.objects.all()
    })

def Vegitable(request):
    return render(request,"Market/Vegitable.html",{
        "Vegitable" : UserFruits.objects.all()
    })

def Lentils(request):
    return render(request,"Market/Lentils.html",{
        "Lentils" : UserFruits.objects.all()
    })

def rice(request):
    return render(request,"Market/rice.html",{
        "Rice" : UserFruits.objects.all()
    })

def grocessory(request):
    return render(request,"Market/grocessory.html",{
        "Grocessory" : UserFruits.objects.all()
    })

def user(request):
    return  render(request,"Market/user.html",{
        "user" : UserFruits.objects.all(),
        "fruits" : Fruits.objects.all()
    })
    


        