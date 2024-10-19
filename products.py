class Product:
    """Represents a product in the store."""

    def __init__(self, name: str, price: float, quantity: int):
        """
        Initialize a product instance.

        :param name: The name of the product.
        :param price: The price of the product.
        :param quantity: The quantity of the product in stock.
        """
        if not name or price < 0 or quantity < 0:
            raise ValueError("Invalid product details")
        self.name = name
        self.price = price
        self.quantity = quantity
        self.active = True
        self.promotion = None

    def set_quantity(self, quantity: int):
        """
        Set the quantity of the product. If the quantity is set to zero, the product is deactivated.

        :param quantity: The quantity to set for the product.
        """
        if quantity < 0:
            raise ValueError("Quantity cannot be negative.")
        self.quantity = quantity
        if self.quantity == 0:
            self.deactivate()

    def get_quantity(self) -> int:
        """
        Return the current quantity of the product.

        :return: The quantity of the product.
        """
        return self.quantity

    def is_active(self) -> bool:
        """
        Check if the product is active.

        :return: True if the product is active, False otherwise.
        """
        return self.active

    def activate(self):
        """
        Activate the product by setting its active status to True.
        """
        self.active = True

    def deactivate(self):
        """
        Deactivate the product by setting its active status to False.
        """
        self.active = False

    def set_promotion(self, promotion):
        """
        Set a promotion for the product.

        :param promotion: The promotion to be applied to the product.
        """
        self.promotion = promotion

    def show(self) -> str:
        """
        Return a string representation of the product.

        :return: A string representing the product details.
        """
        promotion_info = f" (Promotion: {self.promotion.name})" if self.promotion else ""
        return f"{self.name}, Price: €{self.price}, Quantity: {self.quantity}{promotion_info}"

    def buy(self, quantity: int) -> float:
        """
        Purchase a given quantity of the product.

        :param quantity: The number of units to purchase.
        :return: The total price for the purchase.
        :raises Exception: If there is not enough stock or the product is inactive.
        """
        if not self.is_active() or quantity > self.quantity:
            raise Exception("Not enough stock or product inactive.")
        self.quantity -= quantity
        if self.quantity == 0:
            self.deactivate()
        if self.promotion:
            return self.promotion.apply_promotion(self, quantity)
        return self.price * quantity


class NonStockedProduct(Product):
    """Represents a product that doesn't track quantity (e.g., software licenses)."""

    def __init__(self, name: str, price: float):
        super().__init__(name, price, 0)

    def set_quantity(self, quantity: int):
        """
        Prevent changing the quantity for non-stocked products.

        :raises ValueError: Always raises as quantity can't be set for non-stocked products.
        """
        raise ValueError("Cannot set quantity for non-stocked products")

    def buy(self, quantity: int) -> float:
        """
        Purchase a given quantity of the non-stocked product.

        :param quantity: The number of units to purchase.
        :return: The total price for the purchase.
        """
        return self.price * quantity


class LimitedProduct(Product):
    """Represents a product with a purchase limit (e.g., shipping fees)."""

    def __init__(self, name: str, price: float, quantity: int, maximum: int):
        super().__init__(name, price, quantity)
        self.maximum = maximum

    def buy(self, quantity: int) -> float:
        """
        Purchase a given quantity of the limited product.

        :param quantity: The number of units to purchase.
        :return: The total price for the purchase.
        :raises Exception: If the quantity exceeds the purchase limit.
        """
        if quantity > self.maximum:
            raise Exception(f"Cannot buy more than {self.maximum} of this item.")
        return super().buy(quantity)