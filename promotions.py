from abc import ABC, abstractmethod


class Promotion(ABC):
    """Abstract base class for promotions."""

    def __init__(self, name: str):
        """
        Initialize the promotion with a name.

        :param name: The name of the promotion.
        """
        self.name = name

    @abstractmethod
    def apply_promotion(self, product, quantity) -> float:
        """
        Apply the promotion to a product purchase.

        :param product: The product to which the promotion is applied.
        :param quantity: The quantity of the product being purchased.
        :return: The total price after the promotion is applied.
        """
        pass


class PercentDiscount(Promotion):
    """Represents a percentage discount promotion."""

    def __init__(self, name: str, percent: int):
        """
        Initialize the percentage discount promotion.

        :param name: The name of the promotion.
        :param percent: The percentage discount.
        """
        super().__init__(name)
        self.percent = percent

    def apply_promotion(self, product, quantity) -> float:
        """
        Apply the percentage discount to the product.

        :param product: The product to which the discount is applied.
        :param quantity: The quantity of the product being purchased.
        :return: The total price after the discount is applied.
        """
        discount = (self.percent / 100) * product.price
        return (product.price - discount) * quantity


class SecondHalfPrice(Promotion):
    """Represents a promotion where the second item is at half price."""

    def apply_promotion(self, product, quantity) -> float:
        """
        Apply the second half price promotion to the product.

        :param product: The product to which the promotion is applied.
        :param quantity: The quantity of the product being purchased.
        :return: The total price after the promotion is applied.
        """
        full_price_qty = quantity // 2 + quantity % 2
        half_price_qty = quantity // 2
        return full_price_qty * product.price + half_price_qty * product.price * 0.5


class ThirdOneFree(Promotion):
    """Represents a promotion where every third item is free."""

    def apply_promotion(self, product, quantity) -> float:
        """
        Apply the third one free promotion to the product.

        :param product: The product to which the promotion is applied.
        :param quantity: The quantity of the product being purchased.
        :return: The total price after the promotion is applied.
        """
        full_price_qty = quantity - (quantity // 3)
        return full_price_qty * product.price