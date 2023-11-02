from django.db import models
from django.contrib.auth.models import User
import uuid

class Category(models.Model):
    name = models.CharField(max_length=50)
    
    class Meta:
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.name

class Item(models.Model):
    """items which the user can buy"""
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    name = models.CharField(max_length=50) 
    price = models.IntegerField()
    description = models.TextField()        
    image = models.ImageField(upload_to='articles/')

    def __str__(self):
        return self.name[:20]

class Item_in_bag(models.Model):
    """the user's cart of items"""
    username = models.CharField(max_length=50)
    item_id = models.CharField(max_length=50)
    

    def __str__(self):
        return self.username 

class Order_details(models.Model):
    """infos to accept order for the user"""
    owner = models.ForeignKey(User,on_delete=models.CASCADE)
    location = models.CharField(max_length=50)
    date_of_delivery = models.DateTimeField()
    balance = models.IntegerField()
    

    def __str__(self):
        return self.owner.username          

