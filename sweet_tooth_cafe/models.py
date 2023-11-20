import os
import uuid

from django.db import models
from django import forms


# Create your models here.

def generate_unique_name(instance, filename):
    name = uuid.uuid4()  # universally unique id  pic.kenya.png ["kenya", "png"]
    ext = filename.split(".")[-1]
    full_filename = f"{name}.{ext}"
    # full_filename = "%s.%s" % (name, ext)
    return os.path.join("customers", full_filename)


class Wishlist(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)


class Address(models.Model):
    address_name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=13, unique=True)
    country = models.CharField(max_length=100, null=False)
    county = models.CharField(max_length=50, null=False)
    city = models.CharField(max_length=50, null=False)
    zip_code = models.CharField(max_length=10)
    postal_box = models.CharField(max_length=10)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.address_name}'


class Customer(models.Model):

    first_name = models.CharField(max_length=50, null=False)
    last_name = models.CharField(max_length=50, null=False)
    dob = models.DateTimeField()
    gender = models.CharField(max_length=15, default='Rather Not Say')
    email = models.EmailField(unique=True, null=False)
    # address_id = models.ForeignKey(Address, on_delete=models.CASCADE)
    # wishlist_id = models.ForeignKey(Wishlist, on_delete=models.CASCADE)
    is_subscribed = models.BooleanField(default=False)
    profile_pic = models.ImageField(upload_to=generate_unique_name, null=True, default='customers/default.png')
    password = models.CharField(max_length=50,  default='1234567')
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.first_name}, {self.last_name}'


class Inventory(models.Model):
    quantity = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)


class Discount(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)


class Candy(models.Model):
    name = models.CharField(max_length=100)
    brand = models.CharField(max_length=100)
    desc = models.CharField(max_length=500)
    category = models.CharField(max_length=50, null=True, default="Chocolate")
    category_type = models.CharField(max_length=50, null=True, default="Milk")
    #inventory_id = models.ForeignKey(Inventory, on_delete=models.CASCADE)
    cost = models.IntegerField()
    price = models.IntegerField()
    image = models.FileField(upload_to='candies', default='candies/sweets.png')
    #discount_id = models.ForeignKey(Discount, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.brand} {self.name}'

# pip install Pillow
# installs library that supports image uploads


