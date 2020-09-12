from django.db import models

from admin.models import CityModel
from vendor.models import VendorRegistration,FoodItemModel


class CustomerRegistration(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    contact = models.IntegerField(unique=True)
    address = models.TextField()
    city = models.ForeignKey(CityModel,on_delete=models.CASCADE)
    password = models.CharField(max_length=50)
    otp = models.IntegerField()

class OrderModel(models.Model):
    id = models.AutoField(primary_key=True)
    food_item = models.ManyToManyField(FoodItemModel)
    customer = models.ForeignKey(CustomerRegistration,on_delete=models.CASCADE)
    quantity = models.IntegerField()
    total = models.FloatField()
    location = models.TextField()
    date = models.DateField(auto_now_add=True)
    status = models.CharField(max_length=50)

