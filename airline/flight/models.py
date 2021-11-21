from django.db import models

# Create your models here.

class Airport(models.Model):
    code =  models.CharField(max_length=3)
    city = models.CharField(max_length=64)

    def __str__(self):
        return f"{self.city} ({self.code})"


class Flight(models.Model):
    origin = models.ForeignKey(Airport,on_delete=models.CASCADE,related_name="departures")
    destination = models.ForeignKey(Airport,on_delete=models.CASCADE,related_name="arrivals")
    duration = models.IntegerField() 

    def __str__(self):
        return f"{self.id} : {self.origin} to {self.destination}"

class Pasanger(models.Model):
    First_Name = models.CharField(max_length=64)
    Last_Name = models.CharField(max_length=64)
    flight = models.ManyToManyField(Flight,blank=True,related_name="Passanger")

    def __str__(self):
        return f"{self.First_Name} {self.Last_Name}"
