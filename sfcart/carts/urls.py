from django.urls import path
from .views import add_to_cart, cart_items,delete_cart_item, increase_quantity, decrease_quantity


app_name = 'cart'

urlpatterns = [
    path('cart_items/', cart_items, name='cart_items'),
    path('add_to_cart/<int:id>/',add_to_cart, name='add_to_cart'),    
    path('delete/<int:id>/', delete_cart_item, name='delete_cart_item'),
    path('increase/<int:id>/', increase_quantity, name='increase_quantity'),
    path('decrease/<int:id>/', decrease_quantity, name='decrease_quantity'),
]