from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import Pasanger,Flight
# Create your views here.
def index(request):
    return render(request,"flight/index.html",{
        "flight" : Flight.objects.all()
    })

def flight(request,flight_id):
    flight = Flight.objects.get(pk=flight_id)
    return render(request,"flight/flight.html",{
        "flight": flight,
        "Pasanger" : flight.Passanger.all(),
        "non_passanger" : Pasanger.objects.exclude(flight=flight).all()
    })

def book(request,flight_id):
    if request.method == "POST":
        flight = Flight.objects.get(pk=flight_id)
        passanger = Pasanger.objects.get(pk=int(request.POST["passanger"]))
        passanger.flight.add(flight)
        return HttpResponseRedirect(reverse("flight",args=(flight_id,)))


