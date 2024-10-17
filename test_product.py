import pytest
from products import Product

def test_create_normal_product():
    product = Product("MacBook Air M2", price=1450, quantity=100)
    assert product.name == "MacBook Air M2"
    assert product.price == 1450
    assert product.quantity == 100
    assert product.is_active()

def test_create_invalid_product():
    with pytest.raises(ValueError):
        Product("", price=1450, quantity=100)  # Empty name

    with pytest.raises(ValueError):
        Product("MacBook Air M2", price=-10, quantity=100)  # Negative price

def test_product_becomes_inactive():
    product = Product("MacBook Air M2", price=1450, quantity=1)
    product.buy(1)  # Reduce quantity to 0
    assert product.quantity == 0
    assert not product.is_active()

def test_product_purchase_modifies_quantity():
    product = Product("MacBook Air M2", price=1450, quantity=100)
    total_price = product.buy(10)
    assert total_price == 14500  # 10 * 1450
    assert product.quantity == 90

def test_buy_more_than_available():
    product = Product("MacBook Air M2", price=1450, quantity=100)
    with pytest.raises(Exception):
        product.buy(150)  # Trying to buy more than available