from product import Product
from product_manager import ProductManager


def main():
    manager = ProductManager()

    product1 = Product("Laptop", 1200, 5)
    product2 = Product("Mouse", 25, 20)
    product3 = Product("Keyboard", 75, 10)

    manager.add_product(product1)
    manager.add_product(product2)
    manager.add_product(product3)

    print("Available products:")
    manager.display_all_products()

    print(f"\nTotal inventory value: {manager.get_total_inventory_value()}")


if __name__ == "__main__":
    main()