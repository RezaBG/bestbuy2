class Product:
    def __init__(self, name: str, price: float, quantity: int):
        if not name or price < 0 or quantity < 0:
            raise ValueError("Invalid product details")
        self.name = name
        self.price = price
        self.quantity = quantity
        self.active = True

    def get_quantity(self) -> int:
        return self.quantity

    def set_quantity(self, quantity: int):
        if quantity < 0:
            raise ValueError("Quantity cannot be negative.")
        self.quantity = quantity
        if self.quantity == 0:
            self.deactivate()

    def is_active(self) -> bool:
        return self.active

    def activate(self):
        self.active = True

    def deactivate(self):
        self.active = False

    def show(self) -> str:
        return f"{self.name}, Price: €{self.price}, Quantity: {self.quantity}"

    def buy(self, quantity: int) -> float:
        if not self.is_active() or quantity > self.quantity:
            raise Exception("Not enough stock or product inactive.")
        self.quantity -= quantity
        if self.quantity == 0:
            self.deactivate()
        return self.price * quantity


# New Product Types

class NonStockedProduct(Product):
    def __init__(self, name, price):
        super().__init__(name, price, quantity=0)  # Non-stocked products have no quantity

    def set_quantity(self, quantity):
        raise Exception("Non-stocked products don't have a quantity.")

    def show(self):
        return f"{self.name}, Price: €{self.price} (Non-stocked product)"


class LimitedProduct(Product):
    def __init__(self, name, price, quantity, maximum):
        super().__init__(name, price, quantity)
        self.maximum = maximum

    def buy(self, quantity):
        if quantity > self.maximum:
            raise Exception(f"Cannot buy more than {self.maximum} units of this product.")
        return super().buy(quantity)

    def show(self):
        return f"{self.name}, Price: €{self.price}, Quantity: {self.quantity} (Max purchase limit: {self.maximum})"