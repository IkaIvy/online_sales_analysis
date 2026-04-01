class Cart:
    def __init__(self):
        self.cart_items = []

    def add_to_cart(self, product):
        self.cart_items.append(product)

    def calculate_total(self):
        total = 0
        for product in self.cart_items:
            total += product.price
        return total

    def display_cart(self):
        if not self.cart_items:
            print("Cart is empty.")
            return

        print("Products in cart:")
        for product in self.cart_items:
            print(product.display_info())