from product import Product
from product_manager import ProductManager
from cart import Cart


def main():
    manager = ProductManager()

    product1 = Product("Laptop", 1200, 5)
    product2 = Product("Mouse", 25, 20)
    product3 = Product("Keyboard", 75, 10)
    product4 = Product("Monitor", 300, 7)

    manager.add_product(product1)
    manager.add_product(product2)
    manager.add_product(product3)
    manager.add_product(product4)

    print("Available products:")
    manager.display_all_products()

    print(f"\nTotal inventory value: {manager.get_total_inventory_value()}")

    cart = Cart()
    cart.add_to_cart(manager.products[0])
    cart.add_to_cart(manager.products[1])
    cart.add_to_cart(manager.products[2])

    print("\nCart content:")
    cart.display_cart()

    print(f"\nTotal amount to pay: {cart.calculate_total()}")


if __name__ == "__main__":
    main()