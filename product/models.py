from asyncio.windows_events import NULL
from calendar import c
from django.db import models
from django.forms import IntegerField


# Create your models here.
class Author(models.Model):
    name = models.CharField(max_length=255)
    address = models.CharField(max_length=500)


class BookCategory(models.Model):
    name = models.CharField(max_length=255)


class Publisher(models.Model):
    name = models.CharField(max_length=255)
    address = models.CharField(max_length=500)


class Book(models.Model):
    name = models.CharField(max_length=500)
    author = models.ForeignKey(Author, primary_key=False, on_delete=models.CASCADE)
    category = models.ForeignKey(BookCategory, primary_key=False, on_delete=models.CASCADE)
    publisher = models.ForeignKey(Publisher, primary_key=False, on_delete=models.CASCADE)


class Item(models.Model):
    cate = models.IntegerField(default=0)


class BookItem(models.Model):
    price = models.IntegerField(default=0)
    discount = models.FloatField(default=0)
    quantity = models.IntegerField(default=0)
    book = models.ForeignKey(Book, primary_key=False, on_delete=models.CASCADE)
    item = models.ForeignKey(Item, on_delete=models.CASCADE, default=NULL)


class Producer(models.Model):
    name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)


class Type(models.Model):
    desc = models.CharField(max_length=1000)
    detail = models.CharField(max_length=5000)


class Laptop(models.Model):
    name = models.CharField(max_length=255)
    producer = models.ForeignKey(Producer, primary_key=False, on_delete=models.CASCADE)
    type = models.ForeignKey(Type, primary_key=False, on_delete=models.CASCADE)


class LaptopItem(models.Model):
    price = models.IntegerField(default=0)
    quantity = models.IntegerField(default=0)
    laptop = models.ForeignKey(Laptop, primary_key=False, on_delete=models.CASCADE)
    item = models.ForeignKey(Item, on_delete=models.CASCADE, default=NULL)


class Brand(models.Model):
    name = models.CharField(max_length=255)


class Shoes(models.Model):
    name = models.CharField(max_length=255)
    size = models.CharField(max_length=255)
    gender = models.IntegerField(default=0)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    desc = models.CharField(max_length=5000)


class ShoesItem(models.Model):
    price = models.IntegerField(default=0)
    shoes = models.ForeignKey(Shoes, on_delete=models.CASCADE)
    item = models.ForeignKey(Item, on_delete=models.CASCADE, default=NULL)


class Account(models.Model):
    usname = models.CharField(max_length=255)
    passwd = models.CharField(max_length=255)


class Customer(models.Model):
    account = models.ForeignKey(Account, on_delete=models.DO_NOTHING)
    fullname = models.CharField(max_length=255)
    gender = models.IntegerField(default=0)


class Address(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.DO_NOTHING)
    address = models.CharField(max_length=255)
    phone = models.CharField(max_length=12)


class Cart(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.DO_NOTHING, default=0)


class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.DO_NOTHING, default=0)
    item = models.ForeignKey(Item, on_delete=models.DO_NOTHING)
    quantity = models.IntegerField(default=0)


class Image(models.Model):
    item = models.ForeignKey(Item, default=0, on_delete=models.CASCADE)
    urls = models.CharField(max_length=255)


class Shipment(models.Model):
    name = models.CharField(max_length=255)


class Order(models.Model):
    time = models.DateTimeField(auto_now_add=True)
    customer = models.ForeignKey(Customer, on_delete=models.DO_NOTHING)
    shipment = models.ForeignKey(Shipment, on_delete=models.DO_NOTHING)


class Paypal(models.Model):
    order = models.ForeignKey(Order, on_delete=models.DO_NOTHING)
    payID = models.CharField(max_length=255)
    status = models.IntegerField(default=0)


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    item = models.ForeignKey(Item, models.DO_NOTHING)
    quantity = models.IntegerField(default=0)
