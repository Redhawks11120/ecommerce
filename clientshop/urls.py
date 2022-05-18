from django.urls import path
from . import views

urlpatterns = [
     path('',views.Index.as_view(),name="home"),
     path('product',views.Detail.as_view(),name="detail"),
     path('add-cart',views.addCart,name="add to cart"),
     path('cart',views.Cart.as_view(),name="cart"),
     path('change-cart',views.changeCart,name="change-cart"),
     path('checkout',views.Checkout.as_view(),name="checkout"),
     path('payment',views.process_payment,name="payment"),
     path('pay-done',views.PayDone.as_view(),name="paydone")
]