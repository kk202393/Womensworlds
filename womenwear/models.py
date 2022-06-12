from ast import mod
from distutils.command.upload import upload
import email
from email.headerregistry import Address
from email.policy import default
from enum import unique
from locale import currency
from sre_constants import CATEGORY
from telnetlib import STATUS
from time import time
from turtle import update
from typing_extensions import Required
from unicodedata import name
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from autoslug import AutoSlugField
from pkg_resources import require
from num2words import num2words

# Create your models here.
STATE_CHOICES = (
    ("Andaman and Nicobar", "Andaman and Nicobar"),
    ("Andhra Pradesh", "Andhra Pradesh"),
    ("Arunachal Pradesh", "Arunachal Pradesh"),
    ("Assam", "Assam"),
    ("Bihar", "Bihar"),
    ("Chandigarh", "Chandigarh"),
    ("Chhattisgarh", "Chhattisgarh"),
    (
        "Dadra and Nagar Haveli and Daman and Diu",
        "Dadra and Nagar Haveli and Daman and Diu",
    ),
    ("Delhi", "Delhi"),
    ("Goa", "Goa"),
    ("Gujarat ", "Gujarat "),
    ("Haryana", "Haryana"),
    ("Himachal Pradesh", "Himachal Pradesh"),
    ("Jharkhand", "Jharkhand"),
    ("Jammu and Kashmir ", "Jammu and Kashmir "),
    ("Karnataka", "Karnataka"),
    ("Kerala ", "Kerala "),
    ("Lakshadweep", "Lakshadweep"),
    ("Ladakh", "Ladakh"),
    ("Madhya Pradesh", "Madhya Pradesh"),
    ("Maharashtra", "Maharashtra"),
    ("Manipur ", "Manipur "),
    ("Meghalaya ", "Meghalaya "),
    ("Mizoram ", "Mizoram "),
    ("Nagaland ", "Nagaland "),
    ("Odisha ", "Odisha"),
    ("Punjab", "Punjab "),
    ("Puducherry", "Puducherry"),
    ("Rajasthan ", "Rajasthan"),
    ("Sikkim ", "Sikkim "),
    ("Tamil Nadu", "Tamil Nadu"),
    ("Telangana ", "Telangana "),
    ("Tripura ", "Tripura "),
    ("Uttar Pradesh", "Uttar Pradesh"),
    ("Uttarakhand ", "Uttarakhand "),
    ("West Bengal", "West Bengal"),
)
COUNTRY_CHOICES = (
    ("India", "India"),
    ("USA", "USA"),
    ("UK", "UK"),
    ("Australia", "Australia"),
    ("Singapore", "Singapore"),
)


class customer(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=200)
    locality = models.CharField(max_length=100)
    city = models.CharField(max_length=50)
    zipcode = models.IntegerField()
    Mobile_no = models.CharField(max_length=15, default="")
    state = models.CharField(choices=STATE_CHOICES, max_length=60)
    country = models.CharField(choices=COUNTRY_CHOICES, max_length=60, null=False)

    def __str__(self):
        return str(self.id)


CATEGORY_CHOICES = (
    ("1", "Women"),
    ("2", "Husband"),
    ("3", "Kids"),
    ("4", "Jewellery"),
    ("5", "Accessories"),
    ("6", "Personal care"),
    ("7", "Customization"),
    ("8", "Under 799"),
    ("9", "Under 899"),
    ("10", "Under 999"),
)


class product_table(models.Model):
    name = models.CharField(max_length=100)
    main_cat = models.IntegerField()
    sub_cat = models.IntegerField()
    pro_cat = models.IntegerField()
    img = models.ImageField(upload_to="img")
    img2 = models.ImageField(upload_to="img", default="")
    img3 = models.ImageField(upload_to="img", default="")
    img4 = models.ImageField(upload_to="img", default="")
    img5 = models.ImageField(upload_to="img", default="")
    img6 = models.ImageField(upload_to="img", default="")
    img7 = models.ImageField(upload_to="img", default="")
    img8 = models.ImageField(upload_to="img", default="", blank=True)
    desc = models.TextField()
    sell_price = models.IntegerField()
    sell_price_usa = models.IntegerField(null=True)
    art_no = models.CharField(max_length=30)
    disscunt = models.IntegerField()
    actual_price = models.IntegerField()
    actual_price_usa = models.IntegerField(null=True)
    product_slug = AutoSlugField(
        populate_from="name", unique=True, null=True, default=None
    )
    number_of_pieces = models.IntegerField(default="1")
    garment_Length = models.IntegerField(default="1")
    colours = models.CharField(max_length=100, default="")
    top_Fabric = models.CharField(max_length=50, default="")
    bottom_Fabric = models.CharField(max_length=50, default="")
    print = models.CharField(max_length=200, default="")
    closure_Type = models.CharField(max_length=50, default="")
    sleeves_Type = models.CharField(max_length=50, default="")
    hemline = models.CharField(max_length=50, default="")
    transparency = models.IntegerField(default="1")
    weave = models.CharField(max_length=50, default="")
    neckline = models.CharField(max_length=50, default="")
    occasion = models.CharField(max_length=50, default="")
    detailings = models.CharField(max_length=200, default="")
    washing_Instructions = models.CharField(max_length=200, default="")

    def __str__(self):
        return str(self.art_no)

    @property
    def sell_price_usa(self):
        return (self.sell_price + 1500) / 78

    @property
    def actual_price_usa(self):
        return (self.actual_price + 1500) / 78


Country = (
    ("IND", "IND"),
    ("INT", "INT"),
    ("SGP", "SGP"),
    ("AUS", "AUS"),
    ("UK", "UK"),
    ("USA", "USA"),
)
Currency_sign = (
    ("Rs.", "Rs."),
    ("$", "$"),
    ("Au$", "Au$"),
    ("S$", "S$"),
    ("&pound", "&pound"),
)


class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product_table = models.ForeignKey(product_table, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return str(self.id)

    @property
    def total_cost(self):
        return self.quantity * self.product_table.sell_price


STATUS_CHOICES = (
    ("Accepted", "Accepted"),
    ("Packed", "Packed"),
    ("On The Way", "On The Way"),
    ("Delivered", "Delivered"),
    ("Cancel", "Cancel"),
)


class orderPlaced(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    customer = models.ForeignKey(customer, on_delete=models.CASCADE)
    product_table = models.ForeignKey(product_table, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    Total_price = models.IntegerField(default=0)
    ordered_date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=50, choices=STATUS_CHOICES, default="Pending")
    razorpay_payment_id = models.CharField(max_length=150, null=False)
    razorpay_order_id = models.CharField(max_length=200, null=False)
    razorpay_signature = models.CharField(max_length=150, null=False)
    updated_at = models.DateTimeField(auto_now=True)

    @property
    def total_cost(self):
        return self.quantity * self.product_table.sell_price

    @property
    def tax_amount(self):
        return float(self.quantity * self.product_table.sell_price * 0.12)

    @property
    def tax(self):
        return self.quantity * self.product_table.sell_price - self.tax_amount

    @property
    def dis_amount(self):
        return (
            self.quantity * self.product_table.actual_price
            - self.quantity * self.product_table.sell_price
        )

    @property
    def price(self):
        pay_amount = 0.00
        if self.Total_price <= 799:
            pay_amount = self.Total_price + 100
        else:
            pay_amount = self.Total_price
        return pay_amount

    @property
    def priceinwords(self):
        pay_amount = 0.00
        if self.Total_price <= 799:
            pay_amount = self.Total_price + 100
        else:
            pay_amount = self.Total_price
        return num2words(pay_amount)


class oderItem(models.Model):
    order = models.ForeignKey(orderPlaced, on_delete=models.CASCADE)
    product = models.ForeignKey(product_table, on_delete=models.CASCADE)
    price = models.IntegerField(null=False)
    quantity = models.IntegerField(null=False)

    def __str__(self):
        return "{}{}".format(self.orderPlaced.id, self.orderPlaced.tracking_no)


class commonfieldform(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField(max_length=200, default="")
    phone_no = models.CharField(max_length=14)


class Enquiries(commonfieldform):
    whatsapp = models.CharField(max_length=15)
    country = models.CharField(max_length=70)
    enquiry = models.TextField()
    time = models.DateTimeField(auto_now_add=True)


class contact(commonfieldform):
    topic = models.CharField(max_length=200)
    orderid = models.CharField(max_length=100)
    comment = models.TextField()
    time = models.DateTimeField(auto_now_add=True)


class wishlist(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product_table = models.ForeignKey(product_table, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)


class coupon(models.Model):
    coupon = models.CharField(max_length=15)
    discount = models.IntegerField(default=0)
