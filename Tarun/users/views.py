from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth import authenticate,login,logout
from Market.models import Fruits,Vegitables,lentils,Rice,Grocessory,UserFruits

# Create your views here.
def index(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse("login"))
    return render(request,"users/users.html",{
        "Grocessory" : UserFruits.objects.all(),
        "Rice" : UserFruits.objects.all(),
        "Lentils" : UserFruits.objects.all(),
        "Vegitable" : UserFruits.objects.all(),
        "user" : UserFruits.objects.all()
    })

def login_view(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username,password=password)
        if user is  not None:
            login(request,user)
            return HttpResponseRedirect(reverse("index"))
        
        else:
            return render(request,"users/login.html",{"message":"Invalid credential."})

    
    return render(request,"users/login.html")

def logout_view(request):
    logout(request)

    return render(request,"users/login.html",{
        "message":"Successfully Logged Out"
    })