from django.db import models

# Create your models here.
class Demomodel(models.Model):
    name=models.CharField(max_length=50)
    address=models.CharField(max_length=100)
    phone=models.IntegerField()
    mail=models.EmailField()

# class demo(models.Model):
#     num1=models.IntegerField()
#     num2=models.IntegerField()
#     result=models.IntegerField()