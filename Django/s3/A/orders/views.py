from django.shortcuts import render, get_object_or_404, redirect
from django.views import View
from home.models import Product
from .forms import CartAddForm
from .cart import Cart
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Order , OrderItem
class CartView(View):
    def get(self, request):
        cart = Cart(request)
        print(f"Rendering cart page with cart: {cart.cart}")
        return render(request, 'orders/cart.html', {'cart': cart})

class CartAddView(View):
    def post(self, request, product_id):
        cart = Cart(request)
        product = get_object_or_404(Product, id=product_id)
        form = CartAddForm(request.POST)
        if form.is_valid():
            cart.add(product, form.cleaned_data['quantity'])
            print(f"Product {product.name} added to cart with quantity {form.cleaned_data['quantity']}")
        else:
            print("Form is not valid")
        return redirect('orders:cart')


class CartRemoveView(View):
    def get(self , request , product_id):
        cart = Cart(request)
        product = get_object_or_404(Product , id=product_id)
        cart.remove(product)
        return redirect('orders:cart')



class OrderDetailView( LoginRequiredMixin , View):
    def get(self , request , order_id):
        order = get_object_or_404(Order , id=order_id)
        return render(request , 'orders/order.html' , {'order':order})

class OrderCreateView(LoginRequiredMixin , View):
    def get(self , request):
        cart = Cart(request)
        order = Order.objects.create(user=request.user)

        for item in cart:
            OrderItem.objects.create(order = order , product=item['product'] , price=item['price'] , quantity=item['quantity'])
        cart.clear()
        return redirect('orders:order_detail' , order.id)