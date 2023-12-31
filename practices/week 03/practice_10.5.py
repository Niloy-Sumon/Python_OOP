class Customer:
    def __init__(self, email, password):
        self.email = email
        self.password = password
        self.cart = {}

    def add_to_cart(self, product, quantity=1):
        if product in self.cart:
            self.cart[product] += quantity
        else:
            self.cart[product] = quantity
        print(f"{quantity} {product.name}(s) added to your cart.")

    def remove_from_cart(self, product, quantity=1):
        if product in self.cart:
            if self.cart[product] >= quantity:
                self.cart[product] -= quantity
                print(f"{quantity} {product.name}(s) removed from your cart.")
                if self.cart[product] == 0:
                    del self.cart[product]
            else:
                print(f"Insufficient quantity of {product.name} in your cart.")
        else:
            print(f"{product.name} is not in your cart.")

    def view_cart(self):
        if not self.cart:
            print("Your cart is empty.")
        else:
            print("Your cart contains:")
            for product, quantity in self.cart.items():
                print(f"{quantity} x {product.name}")

    def place_order(self, stock):
        if not self.cart:
            print("Your cart is empty. Add products to your cart before placing an order.")
            return

        order_successful = True
        for product, quantity in self.cart.items():
            if product not in stock or stock[product] < quantity:
                print(f"{product.name} is out of stock. Order not placed.")
                order_successful = False
                continue
            stock[product] -= quantity

        if order_successful:
            total_price = sum(product.price * quantity for product, quantity in self.cart.items())
            print(f"Order placed! Total price: ${total_price:.2f}")
            self.cart.clear()

    def __str__(self):
        return f"Customer with email: {self.email}"

class Seller:
    def __init__(self, email, password):
        self.email = email
        self.password = password
        self.products = {}

    def create_product(self, name, price, stock=0):
        product = Product(name, price, stock)
        self.products[product] = stock
        return product

    def list_products(self):
        return self.products

    def __str__(self):
        return f"Seller with email: {self.email}"

class Product:
    def __init__(self, name, price, stock=0):
        self.name = name
        self.price = price
        self.stock = stock

    def __str__(self):
        return f"Product Name: {self.name}, Price: ${self.price:.2f}, Stock: {self.stock}"

# Create sellers
seller1 = Seller("seller1@example.com", "sellerpass1")
seller2 = Seller("seller2@example.com", "sellerpass2")

# Create customers
customer1 = Customer("customer1@example.com", "customerpass1")
customer2 = Customer("customer2@example.com", "customerpass2")

# Sellers add products to sell
product1 = seller1.create_product("Product A", 25.99, stock=10)
product2 = seller1.create_product("Product B", 15.49, stock=5)
product3 = seller2.create_product("Product C", 30.00, stock=3)

# Customers view all available products
print("Available Products:")
for seller in [seller1, seller2]:
    for product, stock in seller.list_products().items():
        if stock > 0:
            print(product)

# Customers add products to their carts
customer1.add_to_cart(product1, 2)
customer1.add_to_cart(product2, 1)
customer2.add_to_cart(product3, 2)

# Customers view their carts
print(f"{customer1}'s cart:")
customer1.view_cart()

# Customers place orders
customer1.place_order(seller1.list_products())
customer2.place_order(seller2.list_products())

# View updated stock
print("Updated Stock:")
for seller in [seller1, seller2]:
    for product, stock in seller.list_products().items():
        print(product)

# Customers view their carts after ordering
print(f"{customer1}'s updated cart:")
customer1.view_cart()
