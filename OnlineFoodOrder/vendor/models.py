from django.db import models
from admin.models import CuisineModel,CityModel

class VendorRegistration(models.Model):
    id = models.AutoField(primary_key=True)
    stall_name = models.CharField(max_length=50)
    contact1 = models.IntegerField(unique=True)
    contact2 = models.IntegerField()
    cuisine_type = models.ForeignKey(CuisineModel,on_delete=models.CASCADE)
    stall_photo = models.ImageField(upload_to='stall_images/')
    address = models.TextField()
    stall_city = models.ForeignKey(CityModel,on_delete=models.CASCADE)
    password = models.CharField(max_length=50)
    otp = models.IntegerField()
    status = models.CharField(max_length=50)

class FoodTypeModel(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    vendor = models.ForeignKey(VendorRegistration,on_delete=models.CASCADE)
    status = models.CharField(max_length=50)

class FoodItemModel(models.Model):
    no = models.AutoField(primary_key=True)
    food_type = models.ForeignKey(FoodTypeModel,on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    price = models.FloatField()
    photo = models.ImageField(upload_to='food_items/')

