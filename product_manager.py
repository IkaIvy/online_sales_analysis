from product import Product


class ProductManager:
    def __init__(self):
        self.products = []

    def add_product(self, product):
        self.products.append(product)

    def display_all_products(self):
        if not self.products:
            print("No products available.")
            return

        for product in self.products:
            print(product.display_info())

    def get_total_inventory_value(self):
        total_value = 0
        for product in self.products:
            total_value += product.price * product.quantity
        return total_value

    def remove_product_by_name(self, name):
        for product in self.products:
            if product.name.lower() == name.lower():
                self.products.remove(product)
                print(f"Product '{name}' removed successfully.")
                return
        print(f"Product '{name}' not found.")