from django.db import models

# Create your models here.
class Fruits(models.Model):
    Fruit = models.CharField(max_length=64)
    Price = models.IntegerField()

    def __str__(self):
        return f"{self.Fruit} : {self.Price}"

class Vegitables(models.Model):
    Vegitable = models.CharField(max_length=64)
    Price = models.IntegerField()

    def __str__(self):
        return f"{self.Vegitable} : {self.Price}"

class lentils(models.Model):
    Lentil = models.CharField(max_length=64)
    Price = models.IntegerField()

    def __str__(self):
        return f"{self.Lentil} : {self.Price}"

class Rice(models.Model):
    rice = models.CharField(max_length=64)
    Price = models.IntegerField()
    
    def __str__(self):
        return f"{self.rice} : {self.Price}"

class Grocessory(models.Model):
    grocessory = models.CharField(max_length=64)    
    Price = models.IntegerField()
    def  __str__(self):
        return f"{self.grocessory} : {self.Price}"

class UserFruits(models.Model):
    Fruit = models.ForeignKey(Fruits,on_delete=models.CASCADE,related_name="fruit")
    Vegitable = models.ForeignKey(Vegitables,on_delete=models.CASCADE,related_name="Vegitabl")
    lentil = models.ForeignKey(lentils,on_delete=models.CASCADE,related_name="lentil")
    rice = models.ForeignKey(Rice,on_delete=models.CASCADE,related_name="Ricee")
    Grocessory = models.ForeignKey(Grocessory,on_delete=models.CASCADE,related_name="Grocessory")


