class Product:
    def __init__(self, name: str, price: float, quantity: int):
        if not name or price < 0 or quantity < 0:
            raise ValueError("Invalid product details")
        self._name = name
        self._price = price
        self._quantity = quantity
        self.active = True
        self.promotion = None

    @property
    def name(self):
        return self._name

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, new_price):
        if new_price < 0:
            raise ValueError("Price cannot be negative.")
        self._price = new_price

    @property
    def quantity(self):
        return self._quantity

    @quantity.setter
    def quantity(self, new_quantity):
        if new_quantity < 0:
            raise ValueError("Quantity cannot be negative.")
        self._quantity = new_quantity
        if self._quantity == 0:
            self.deactivate()

    def is_active(self) -> bool:
        return self.active

    def activate(self):
        self.active = True

    def deactivate(self):
        self.active = False

    def __str__(self) -> str:
        promotion_info = f" (Promotion: {self.promotion.name})" if self.promotion else ""
        return f"{self.name}, Price: €{self.price}, Quantity: {self.quantity}{promotion_info}"

    def __gt__(self, other):
        if isinstance(other, Product):
            return self.price > other.price
        return NotImplemented

    def __lt__(self, other):
        if isinstance(other, Product):
            return self.price < other.price
        return NotImplemented

    def buy(self, quantity: int) -> float:
        if not self.is_active() or quantity > self.quantity:
            raise Exception("Not enough stock or product inactive.")
        self.quantity -= quantity
        if self.quantity == 0:
            self.deactivate()

        if self.promotion:
            return self.promotion.apply_promotion(self, quantity)

        return self.price * quantity


# Define the new product types using inheritance

class NonStockedProduct(Product):
    def __init__(self, name: str, price: float):
        # NonStockedProduct always has a quantity of 0
        super().__init__(name, price, quantity=0)

    def set_quantity(self, quantity: int):
        # Quantity is always 0 for non-stocked products
        raise ValueError("Cannot set quantity for non-stocked product")

    def buy(self, quantity: int) -> float:
        # Buying any quantity is always allowed for non-stocked products
        return self.price * quantity


class LimitedProduct(Product):
    def __init__(self, name: str, price: float, quantity: int, maximum: int):
        super().__init__(name, price, quantity)
        self.maximum = maximum

    def buy(self, quantity: int) -> float:
        if quantity > self.maximum:
            raise Exception(f"Cannot buy more than {self.maximum} of this item.")
        return super().buy(quantity)