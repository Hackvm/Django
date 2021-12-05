from django.urls import  path
from . import views

urlpatterns = [
    path("",views.index,name="index"),
    path("user",views.user,name="user"),
    path("Vegitable",views.Vegitable,name="Vegitable"),
    path("rice",views.rice,name="rice"),
    path("Lentils",views.Lentils,name="Lentils"),
    path("grocessory",views.grocessory,name="grocessory")

]