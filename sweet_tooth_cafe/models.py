import os
import uuid
from datetime import datetime

from django.db import models
from django import forms


# Create your models here.

def generate_unique_name(instance, filename):
    name = uuid.uuid4()  # universally unique id  pic.kenya.png ["kenya", "png"]
    ext = filename.split(".")[-1]
    full_filename = f"{name}.{ext}"
    # full_filename = "%s.%s" % (name, ext)
    return os.path.join("customers", full_filename)


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
    GENDER = [
        ('Female', 'Female'),
        ('Male', 'Male'),
        ('Other', 'Other'),
    ]
    first_name = models.CharField(max_length=50, null=False)
    last_name = models.CharField(max_length=50, null=False)
    dob = models.DateTimeField()
    gender = models.CharField(max_length=15, choices=GENDER, default='Other')
    email = models.EmailField(unique=True, null=False)
    username = models.CharField(max_length=50, default='', null=False)
    address_id = models.OneToOneField(Address, on_delete=models.PROTECT, blank=True, null=True)
    is_subscribed = models.BooleanField(default=False)
    profile_pic = models.ImageField(upload_to=generate_unique_name, null=True, default='customers/default.png')
    password = models.CharField(max_length=50, default='1234567')
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.first_name}, {self.last_name}'


class Discount(models.Model):
    name = models.CharField(max_length=50, default='')
    code = models.CharField(max_length=50, default='', unique=True)
    amount = models.IntegerField(default=100)
    min_spend = models.IntegerField(default=300)
    max_discount = models.IntegerField(default=500)
    expires_on = models.DateTimeField(default=datetime.now, blank=True)
    is_active = models.BooleanField(default=False)
    image = models.ImageField(upload_to='deals', default='', null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.name}'


class Candy(models.Model):
    CATEGORIES = [
        ('Chocolate', 'Chocolate'),
        ('Gum', 'Gum'),
        ('Gummys', 'Gummys'),
        ('Jelly Beans', 'Jelly Beans'),
        ('Licorice', 'Licorice'),
        ('Marshmallows', 'Marshmallows'),
        ('Sweets', 'Sweets'),
        ('Taffy', 'Taffy'),
        ('Cookies', 'Cookies'),
    ]
    FLAVOURS = [
        ('Berry', 'Berry'),
        ('Bubble Gum', 'Bubble Gum'),
        ('Butter', 'Butter'),
        ('Buttered Popcorn', 'Buttered Popcorn'),
        ('Caramel', 'Caramel'),
        ('Chocolate', 'Chocolate'),
        ('Cream', 'Cream'),
        ('Dark', 'Dark'),
        ('Eclairs', 'Eclairs'),
        ('Fruit', 'Fruit'),
        ('Fudge', 'Fudge'),
        ('Lemon', 'Lemon'),
        ('Menthol', 'Menthol'),
        ('Milk', 'Milk'),
        ('Mint', 'Mint'),
        ('Orange', 'Orange'),
        ('Strawberry', 'Strawberry'),
        ('Sour', 'Sour'),
        ('Top Deck', 'Top Deck'),
        ('Toffee', 'Toffee'),
        ('Vanilla', 'Vanilla'),
        ('Watermelon', 'Watermelon'),
        ('White', 'White'),

    ]

    category_name = models.CharField(max_length=50, default='', choices=CATEGORIES)
    flavour = models.CharField(max_length=50, null=True, default='', choices=FLAVOURS)
    add_ons = models.CharField(max_length=50, null=True, default='Plain')
    brand = models.CharField(max_length=100)
    quantity = models.IntegerField(null=True, default=0)
    weight = models.FloatField(null=True, default=0)
    in_inventory = models.IntegerField(default=0, null=True)
    price = models.IntegerField(null=True, default=0)
    rating = models.IntegerField(default=0)
    image = models.FileField(upload_to='candies', default='candies/sweets.png')
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    discount_id = models.ForeignKey(Discount, on_delete=models.PROTECT, blank=True, null=True)

    def __str__(self):
        if self.add_ons != 'Plain':
            connector = 'with '
        else:
            connector = ''
        return f'{self.brand} {self.flavour} {self.category_name} {connector} {self.add_ons} - {self.weight}g '


class Cart(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.PROTECT, null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.id} {self.customer}'


class CartItem(models.Model):
    cart_id = models.ForeignKey(Cart, on_delete=models.CASCADE, null=False)
    candy = models.ForeignKey(Candy, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.candy}'


class Payment(models.Model):
    PAYMENT_TYPES = [
        ('Cash', 'Cash'),
        ('Mpesa', 'Mpesa'),
    ]
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, null=False)
    payment_type = models.CharField(choices=PAYMENT_TYPES, null=False, max_length=20)
    account = models.CharField(null=True, max_length=20)

    def __str__(self):
        return f'{self.payment_type}'


class Order(models.Model):
    STATUS = [
        ('Canceled', 'Canceled'),
        ('Completed', 'Completed'),
        ('In Process', 'In Process'),
        ('Pending', 'Pending'),
        ('Processing', 'Processing'),

    ]
    customer = models.ForeignKey(Customer, on_delete=models.PROTECT, null=False)
    candy = models.ManyToManyField(Candy)
    to_deliver = models.BooleanField(default=True)
    total = models.IntegerField()
    order_status = models.CharField(choices=STATUS, default=STATUS[3], max_length=50)
    discount_id = models.ForeignKey(Discount, on_delete=models.PROTECT, null=True, blank=True)
    payment = models.ForeignKey(Payment, on_delete=models.CASCADE, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.id}{self.customer}'


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.PROTECT, null=False)
    candy = models.ForeignKey(Candy, on_delete=models.PROTECT, null=True)
    quantity = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.candy}'


class Wishlist(models.Model):
    customer = models.OneToOneField(Customer, on_delete=models.PROTECT, null=True, default=0)
    list_name = models.CharField(max_length=50, default='Default')
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.customer.first_name}'s Wishlist"


class WishlistList(models.Model):
    name = models.CharField(default='Default', max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.name}'


class WishListItem(models.Model):
    list_id = models.ForeignKey(WishlistList, on_delete=models.CASCADE, null=False, default='Default')
    candy = models.ForeignKey(Candy, on_delete=models.CASCADE, null=False)
    quantity = models.IntegerField()


# pip install Pillow
# installs library that supports image uploads
