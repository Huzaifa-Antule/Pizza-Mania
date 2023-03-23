from django.db import models

# Create your models here.
class Contact(models.Model):
    name = models.CharField( max_length=100)
    email= models.CharField( max_length=150)
    number= models.CharField( max_length=12) 
    desc= models.TextField()
    date = models.DateField()
    
                #  Order Models

class Order(models.Model):
    name = models.CharField( max_length=100)
    number= models.CharField( max_length=150)
    number1= models.CharField( max_length=12) 
    total_bill =models.TextField() 
    Onion_pizza =models.TextField() 
    Sweet_Corn_pizza=models.TextField() 
    Address= models.TextField()
    date = models.DateField()

