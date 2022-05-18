import uuid
from django.http import HttpResponse
from django.shortcuts import render
from django.views import View
from product import models
from django.contrib import messages
from django.conf import settings
from decimal import Decimal
from paypal.standard.forms import PayPalPaymentsForm


# Create your views here.
class Index(View):
    def get(_seft, _request):
        cart = models.Cart.objects.get(customer=1)
        items = models.CartItem.objects.filter(cart=cart.id)
        page = _request.GET.get('page')
        queryset = models.Item.objects.all();
        products = []
        for product in queryset:
            image = models.Image.objects.get(item=product.id)
            if (product.cate == 0):
                book = models.BookItem.objects.filter(item=product.id)
                detail = book[0].book;
                products.append({'id': product.id, 'url': image.urls, "name": detail.name, "price": book[0].price})
            else:
                if (product.cate == 1):
                    shoes = models.ShoesItem.objects.filter(item=product.id)
                    detail = shoes[0].shoes;
                    products.append({'id': product.id, 'url': image.urls, 'name': detail.name, 'price': shoes[0].price})
                else:
                    if (product.cate == 2):
                        laptop = models.LaptopItem.objects.filter(item=product.id)
                        detail = laptop[0].laptop;
                        products.append(
                            {'id': product.id, 'url': image.urls, 'name': detail.name, 'price': laptop[0].price})
        context = {"page": page, "products": products, "cart": len(items)}
        return render(_request, 'index.html', context)

    def post(_seft, _request):
        _seft.get(_request)


class Detail(View):
    def get(_seft, _request):
        cart = models.Cart.objects.get(customer=1)
        items = models.CartItem.objects.filter(cart=cart.id)
        pid = _request.GET.get('pid')
        product = models.Item.objects.get(pk=pid)
        products = None
        image = models.Image.objects.get(item=product.id)
        if (product.cate == 0):
            book = models.BookItem.objects.get(item=product.id)
            detail = book.book;
            author = book.book.author.name;
            publisher = book.book.publisher.name;
            category = book.book.category.name;
            products = {'cate': product.cate, 'id': product.id, 'url': image.urls, "name": detail.name,
                        "price": book.price, "author": author, "publisher": publisher, "category": category}
        elif (product.cate == 1):
            shoes = models.ShoesItem.objects.filter(item=product.id)
            detail = shoes[0].shoes;
            products = {'cate': product.cate, 'id': product.id, 'url': image.urls, 'name': detail.name,
                        'price': shoes[0].price}
        elif (product.cate == 2):
            laptop = models.LaptopItem.objects.filter(item=product.id)
            detail = laptop[0].laptop;
            products = {'cate': product.cate, 'id': product.id, 'url': image.urls, 'name': detail.name,
                        'price': laptop[0].price}
        context = {"products": products, "cart": len(items)}
        return render(_request, 'detail.html', context)

    def post(_seft, _request):
        _seft.get(_request)


def addCart(_request):
    item = _request.GET.get('product')
    quan = _request.GET.get('quantity')
    try:
        cart = models.Cart.objects.get(customer=1)
        items = models.CartItem.objects.get(cart=cart.id, item=item)
        if items is not None:
            items.quantity = items.quantity + int(quan)
            items.save()
        else:
            item = models.CartItem(cart=cart, item=models.Item.objects.get(pk=item), quantity=quan)
            item.save()
    except:
        items = models.CartItem(cart=cart, item=models.Item.objects.get(pk=item), quantity=quan)
        items.save()
    return HttpResponse(_request, 'done');


class Cart(View):
    def get(_seft, _request):
        products = []
        sum = 0
        try:
            cart = models.Cart.objects.get(customer=1)
            items = models.CartItem.objects.filter(cart=cart.id)
            for item in items:
                product = item.item;
                quantity = item.quantity;
                image = models.Image.objects.get(item=product.id)
                if (product.cate == 0):
                    book = models.BookItem.objects.filter(item=product.id)
                    detail = book[0].book;
                    total = int(book[0].price) * int(quantity)
                    sum += total;
                    products.append(
                        {'cartit': item.id, 'total': total, 'quantity': quantity, 'id': product.id, 'url': image.urls,
                         "name": detail.name, "price": book[0].price})
                else:
                    if (product.cate == 1):
                        shoes = models.ShoesItem.objects.filter(item=product.id)
                        detail = shoes[0].shoes;
                        total = int(shoes[0].price) * int(quantity)
                        sum += total;
                        products.append({'cartit': item.id, 'total': total, 'quantity': quantity, 'id': product.id,
                                         'url': image.urls, 'name': detail.name, 'price': shoes[0].price})
                    else:
                        if (product.cate == 2):
                            laptop = models.LaptopItem.objects.filter(item=product.id)
                            detail = laptop[0].laptop;
                            total = int(laptop[0].price) * int(quantity)
                            sum += total;
                            products.append({'cartit': item.id, 'total': total, 'quantity': quantity, 'id': product.id,
                                             'url': image.urls, 'name': detail.name, 'price': laptop[0].price})
        except:
            products = []

        return render(_request, 'cart.html', {"products": products, "sum": sum})


def changeCart(_request):
    item = _request.POST.get('item')
    quantity = _request.POST.get('quantity')
    it = models.CartItem.objects.get(pk=item)
    it.quantity = quantity
    it.save()
    if int(it.quantity) <= 0:
        it.delete()
    return HttpResponse(_request, 'done')


class Checkout(View):
    def get(_seft, _request):
        products = []
        sum = 0
        address = models.Address.objects.filter(customer=1)
        account = models.Customer.objects.get(pk=1)
        try:
            cart = models.Cart.objects.get(customer=1)
            items = models.CartItem.objects.filter(cart=cart.id)
            for item in items:
                product = item.item;
                quantity = item.quantity;
                image = models.Image.objects.get(item=product.id)
                if (product.cate == 0):
                    book = models.BookItem.objects.filter(item=product.id)
                    detail = book[0].book;
                    total = int(book[0].price) * int(quantity)
                    sum += total;
                    products.append(
                        {'cartit': item.id, 'total': total, 'quantity': quantity, 'id': product.id, 'url': image.urls,
                         "name": detail.name, "price": book[0].price})
                else:
                    if (product.cate == 1):
                        shoes = models.ShoesItem.objects.filter(item=product.id)
                        detail = shoes[0].shoes;
                        total = int(shoes[0].price) * int(quantity)
                        sum += total;
                        products.append({'cartit': item.id, 'total': total, 'quantity': quantity, 'id': product.id,
                                         'url': image.urls, 'name': detail.name, 'price': shoes[0].price})
                    else:
                        if (product.cate == 2):
                            laptop = models.LaptopItem.objects.filter(item=product.id)
                            detail = laptop[0].laptop;
                            total = int(laptop[0].price) * int(quantity)
                            sum += total;
                            products.append({'cartit': item.id, 'total': total, 'quantity': quantity, 'id': product.id,
                                             'url': image.urls, 'name': detail.name, 'price': laptop[0].price})
        except:
            products = []

        return render(_request, 'checkout.html',
                      {"products": products, "sum": sum, "address": address, "cart": len(products), "acc": account})


# def checkout(request):
#     #...

def process_payment(request):
    customer = models.Customer.objects.get(pk=1)
    shipment = models.Shipment.objects.get(pk=1)
    order = models.Order(customer=customer, shipment=shipment)
    order.save()
    total = request.POST.get('total');
    cart = models.Cart.objects.get(customer=customer.id)
    orderid = uuid.uuid4();
    paypal_dict = {
        'business': settings.PAYPAL_RECEIVER_EMAIL,
        'amount': total,
        'item_name': 'Order ' + str(orderid),
        'invoice': str(orderid),
        'currency_code': 'USD',
        'notify_url': 'http://localhost:8000/pay-done?order=' + str(order.id),
        'return_url': 'http://localhost:8000/pay-done?order=' + str(order.id),
        'cancel_return': '/pay-done?order=' + str(order.id)
    }
    paypal = models.Paypal(order=order, payID=orderid, status=0)
    paypal.save()
    form = PayPalPaymentsForm(initial=paypal_dict)
    return render(request, 'payment.html', {'form': form})


class PayDone(View):
    def get(_seft, _request):
        order = _request.GET.get('order');
        orderi = models.Order.objects.get(pk=order)
        customer = orderi.customer;
        paypal = models.Paypal.objects.get(order=order);
        paypal.status = 1
        paypal.save()
        cart = models.Cart.objects.get(customer=customer.id)
        listcarti = models.CartItem.objects.filter(cart=cart.id)
        for i in listcarti:
            i.delete()
        return render(_request, 'paydone.html')
