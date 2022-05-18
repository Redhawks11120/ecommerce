from django.contrib import admin
from . import models

db_tb = [models.Account,models.Address,models.Author,
models.Book,models.BookCategory,models.BookItem,models.Brand,
models.Cart,models.Customer,
models.Image,
models.Laptop,models.LaptopItem,
models.Order,
models.Paypal,models.Producer,models.Publisher,
models.Shipment,models.Shoes,models.ShoesItem,
models.Type,
models.Item,
models.CartItem]

admin.site.register(db_tb)
