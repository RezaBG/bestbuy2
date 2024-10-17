class Store:
    def __init__(self, products: list):
        self.products = products

    def add_product(self, product):
        self.products.append(product)

    def remove_product(self, product):
        self.products.remove(product)

    def get_total_quantity(self) -> int:
        return sum([product.quantity for product in self.products])

    def get_all_products(self):
        return [product for product in self.products if product.is_active()]

    def order(self, shopping_list: list) -> float:
        total_price = 0
        for product, quantity in shopping_list:
            total_price += product.buy(quantity)
        return total_price

    def __contains__(self, product) -> bool:
        return product in self.products

    def __add__(self, other_store):
        combined_products = self.products + other_store.products
        return Store(combined_products)