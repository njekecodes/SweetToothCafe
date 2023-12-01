import os
import uuid
from datetime import datetime, time

from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import User, Group
from django.db import models


# Create your models here.

def generate_unique_name(instance, filename):
    name = uuid.uuid4()  # universally unique id  pic.kenya.png ["kenya", "png"]
    ext = filename.split(".")[-1]
    full_filename = f"{name}.{ext}"
    # full_filename = "%s.%s" % (name, ext)
    return os.path.join("customers", full_filename)


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
    is_subscribed = models.BooleanField(default=False)
    profile_pic = models.ImageField(upload_to=generate_unique_name, null=True, default='customers/default.png')
    password = models.CharField(max_length=50, default='1234567')
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    USERNAME_FIELD = 'email' or 'username'

    def __str__(self):
        return f'{self.first_name}, {self.last_name}'


class Address(models.Model):
    COUNTRIES = [
        ('Kenya', 'Kenya'),
        ('Uganda', 'Uganda'),
        ('Tanzania', 'Tanzania'),
    ]
    if COUNTRIES[0]:
        COUNTIES = [
            (1, 'Mombasa'),
            (2, 'Kwale'),
            (3, 'Kilifi'),
            (4, 'Tana River'),
            (5, 'Lamu'),
            (6, 'Taita Taveta'),
            (7, 'Garissa'),
            (8, 'Wajir'),
            (9, 'Mandera'),
            (10, 'Marsabit'),
            (11, 'Isiolo'),
            (12, 'Meru'),
            (13, 'Tharaka - Nithi'),
            (14, 'Embu'),
            (15, 'Kitui'),
            (16, 'Machakos'),
            (17, 'Makueni'),
            (18, 'Nyandarua'),
            (19, 'Nyeri'),
            (20, 'Kirinyaga'),
            (21, 'Murang’a'),
            (22, 'Kiambu'),
            (23, 'Turkana'),
            (24, 'West Pokot'),
            (25, 'Samburu'),
            (26, 'Trans-Nzoia'),
            (27, 'Uasin-Gishu'),
            (28, 'Elgeyo - Marakwet'),
            (29, 'Nandi'),
            (30, 'Baringo'),
            (31, 'Laikipia'),
            (32, 'Nakuru'),
            (33, 'Narok'),
            (34, 'Kajiado'),
            (35, 'Kericho'),
            (36, 'Bomet'),
            (37, 'Kakamega'),
            (38, 'Vihiga'),
            (39, 'Bungoma'),
            (40, 'Busia'),
            (41, 'Siaya'),
            (42, 'Kisumu'),
            (43, 'Homa Bay'),
            (44, 'Migori'),
            (45, 'Kisii'),
            (46, 'Nyamira'),
            (47, 'Nairobi'),
        ]
        customer = models.OneToOneField(Customer, on_delete=models.CASCADE, default=0)
        address_name = models.CharField(max_length=100)
        phone_number = models.CharField(max_length=13, unique=True)
        country = models.CharField(max_length=100, null=False, choices=COUNTRIES)
        county = models.CharField(max_length=50, null=True, choices=COUNTIES)
        city = models.CharField(max_length=50, null=False)
        zip_code = models.CharField(max_length=10)
        postal_box = models.CharField(max_length=10)
        created_at = models.DateTimeField(auto_now_add=True)
        modified_at = models.DateTimeField(auto_now=True)

        def __str__(self):
            return f'{self.address_name}'


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
    weight = models.DecimalField(null=True, default=0, decimal_places=2, max_digits=10)
    in_inventory = models.IntegerField(default=0, null=True)
    price = models.IntegerField(null=True, default=0)
    rating = models.IntegerField(default=0)
    image = models.FileField(upload_to='candies', default='candies/sweets.png')
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    discount_id = models.ForeignKey(Discount, on_delete=models.PROTECT, blank=True, null=True,
                                    related_name='candies')

    def __str__(self):
        if self.add_ons != 'Plain':
            connector = 'with '
        else:
            connector = ''
        return f'{self.brand} {self.flavour} {self.category_name} {connector} {self.add_ons} - {self.weight}g '


class Cart(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.id} {self.customer}'


class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, null=False)
    candy = models.ForeignKey(Candy, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)


def __str__(self):
    return f'{self.candy.__str__()}'


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
    customer = models.ForeignKey(Customer, on_delete=models.PROTECT, null=False, related_name='customer_order')
    to_deliver = models.BooleanField(default=True)
    total = models.DecimalField(max_digits=8, decimal_places=2)
    order_status = models.CharField(choices=STATUS, default=STATUS[3], max_length=50)
    discount_id = models.ForeignKey(Discount, on_delete=models.CASCADE, null=True, blank=True)
    payment = models.ForeignKey(Payment, on_delete=models.CASCADE, null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.id}{self.customer}'


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.PROTECT, null=False, related_name='order')
    candy = models.ForeignKey(Candy, on_delete=models.PROTECT, null=True, related_name='candy')
    quantity = models.IntegerField(default=0)
    price = models.DecimalField(max_digits=8, decimal_places=2, default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.candy.__str__()}'


class Wishlist(models.Model):
    pass

class WishlistList(models.Model):
    pass

class WishListItem(models.Model):
    pass

# pip install Pillow
# installs library that supports image uploads
