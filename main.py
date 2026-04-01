from product import Product
from product_manager import ProductManager


def main():
    manager = ProductManager()

    product1 = Product("Gaming Laptop", 1500, 3)
    product2 = Product("Wireless Mouse", 40, 15)
    product3 = Product("Mechanical Keyboard", 100, 8)

    manager.add_product(product1)
    manager.add_product(product2)
    manager.add_product(product3)


if __name__ == "__main__":
    main()