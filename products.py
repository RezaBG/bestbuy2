class Product:
    def __init__(self, name: str, price: float, quantity: int):
        if not name or price < 0 or quantity < 0:
            raise ValueError("Invalid product details")
        self.name = name
        self.price = price
        self.quantity = quantity
        self.active = True
        self.promotion = None  # Add a promotion attribute

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
        promotion_info = f" (Promotion: {self.promotion.name})" if self.promotion else ""
        return f"{self.name}, Price: €{self.price}, Quantity: {self.quantity}{promotion_info}"

    def buy(self, quantity: int) -> float:
        if not self.is_active() or quantity > self.quantity:
            raise Exception("Not enough stock or product inactive.")
        self.quantity -= quantity
        if self.quantity == 0:
            self.deactivate()
        if self.promotion:  # Apply promotion if it exists
            return self.promotion.apply_promotion(self, quantity)
        return self.price * quantity

    def set_promotion(self, promotion):
        """Sets a promotion for the product."""
        self.promotion = promotion