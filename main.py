from product import Product
from product_manager import ProductManager
from cart import Cart


def main():
    manager = ProductManager()

    product1 = Product("Gaming Laptop", 1500, 3)
    product2 = Product("Wireless Mouse", 40, 15)
    product3 = Product("Mechanical Keyboard", 100, 8)
    product4 = Product("Monitor", 300, 7)

    manager.add_product(product1)
    manager.add_product(product2)
    manager.add_product(product3)
    manager.add_product(product4)

    cart = Cart()
    cart.add_to_cart(manager.products[0])
    cart.add_to_cart(manager.products[1])
    cart.add_to_cart(manager.products[2])

    print("Cart content:")
    cart.display_cart()

    print(f"\nTotal amount to pay: {cart.calculate_total()}")


if __name__ == "__main__":
    main()