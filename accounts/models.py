from django.db import models

# Create your models here.
class student(models.Model):
    
    name=models.CharField(max_length=100)
    age=models.IntegerField(default=18)
    address=models.TextField(null=True,blank=False)
   

class Car(models.Model):
    car_name=models.CharField(max_length=100)
    speed=models.IntegerField()

    def __str__(self)->str:
        return self.car_name