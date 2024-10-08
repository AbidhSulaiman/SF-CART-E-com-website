from django.shortcuts import render, get_object_or_404, redirect
from products.models import Product
from .models import Cart, CartItem
from django.contrib import messages
from django.http import JsonResponse

# Create your views here.


def add_to_cart(request, id):

    product = get_object_or_404(Product, id = id)

    cart,created = Cart.objects.get_or_create(user = request.user)
    cart_item, created = CartItem.objects.get_or_create(cart=cart, product=product)

    if not created:
        cart_item.quantity += 1
    cart_item.save()


    messages.success(request, f'{product.name} has been added to your cart.')
    return redirect('products:product_detail', id=product.id)

def cart_items(request):

    cart = Cart.objects.get(user=request.user)
    cart_items = cart.items.all()

    context = {'cart_items':cart_items,'cart':cart }
    return render(request, 'carts/cart_details.html', context)

def delete_cart_item(request, id):

    if request.method == 'POST':
        cart = get_object_or_404(Cart, user=request.user)
        cart_item = get_object_or_404(cart.items, id=id)
        cart_item.delete()

        return redirect('cart:cart_items')
    return render(request, 'carts/cart_details.html')



def increase_quantity(request, id):
    cart = get_object_or_404(Cart, user=request.user)
    cart_item = get_object_or_404(CartItem, cart=cart, id=id)

    cart_item.quantity += 1
    cart_item.save()

    # Return updated quantity and total price
    return JsonResponse({
        'quantity': cart_item.quantity,
        'total_price': cart_item.product.price * cart_item.quantity
    })


def decrease_quantity(request, id):
    cart = get_object_or_404(Cart, user=request.user)
    cart_item = get_object_or_404(CartItem, cart=cart, id=id)

    if cart_item.quantity > 1:
        cart_item.quantity -= 1
        cart_item.save()

        # Return updated quantity and total price
        return JsonResponse({
            'quantity': cart_item.quantity,
            'total_price': cart_item.product.price * cart_item.quantity
        })
    else:
        cart_item.delete()

        return JsonResponse({
            'quantity': 0,
            'deleted': True
        })
