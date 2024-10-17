from abc import ABC, abstractmethod

class Promotion(ABC):
    def __init__(self, name: str):
        self.name = name

    @abstractmethod
    def apply_promotion(self, product, quantity) -> float:
        pass


class PercentDiscount(Promotion):
    def __init__(self, name: str, percent: int):
        super().__init__(name)
        self.percent = percent

    def apply_promotion(self, product, quantity) -> float:
        discount = (self.percent / 100) * product.price
        return (product.price - discount) * quantity


class SecondHalfPrice(Promotion):
    def apply_promotion(self, product, quantity) -> float:
        full_price_qty = quantity // 2 + quantity % 2
        half_price_qty = quantity // 2
        return full_price_qty * product.price + half_price_qty * product.price * 0.5


class ThirdOneFree(Promotion):
    def apply_promotion(self, product, quantity) -> float:
        full_price_qty = quantity - (quantity // 3)
        return full_price_qty * product.price