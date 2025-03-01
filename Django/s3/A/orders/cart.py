from home.models import Product

CART_SESSION_ID = 'cart'

class Cart:
    def __init__(self, request):
        self.session = request.session
        cart = self.session.get(CART_SESSION_ID)
        if not cart:
            cart = self.session[CART_SESSION_ID] = {}
        self.cart = cart
        print(f"Cart initialized: {self.cart}")

    def __iter__(self):
        product_ids = self.cart.keys()
        products = Product.objects.filter(id__in=product_ids) #only producs with has taht product id -> it iters in the product_ids
        cart = self.cart.copy()
        for product in products:
            cart[str(product.id)]['product'] = product
        for item in cart.values():
            item['total_price'] = int(item['price']) * int(item['quantity'])
            print(f"Iterating over item: {item}")
            yield item

    def __len__(self): #the nubmer of items in cart in navbar
        return sum(item['quantity'] for item in self.cart.values())
    def add(self, product, quantity):
        product_id = str(product.id) #sessions accept string
        if product_id not in self.cart:
            self.cart[product_id] = {'quantity': 0, 'price': str(product.price)}
        self.cart[product_id]['quantity'] += quantity
        self.save()
        print(f"Added {quantity} of {product.name} to cart. Cart now has: {self.cart}")

    def save(self):
        self.session.modified = True

    def get_total_price(self):
        return sum(int(item['price']) * item['quantity'] for item in self.cart.values())

    def remove(self , product):
        product_id = str(product.id) #sessions accept string
        if product_id in self.cart:
            del self.cart[product_id]
            self.save()

    def clear(self):
        del self.session[CART_SESSION_ID]
        self.save()