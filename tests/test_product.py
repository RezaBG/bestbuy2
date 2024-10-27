import pytest
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from products import Product, NonStockedProduct, LimitedProduct
from promotions import PercentDiscount, SecondHalfPrice, ThirdOneFree

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

# New tests for NonStockedProduct
def test_nonstocked_product():
    """Test that NonStockedProduct behaves correctly."""
    product = NonStockedProduct("Windows License", price=125)
    assert product.get_quantity() == 0
    assert product.is_active()
    # Ensure show method displays "Quantity: Unlimited" correctly
    assert product.show() == "Windows License, Price; $125, Quantity: Unlimited"

    # Attempting to set quantity should raise an error
    with pytest.raises(ValueError):
        product.set_quantity(10)

# New tests for LimitedProduct
def test_limited_product():
    """Test that LimitedProduct behaves correctly when purchase limit is exceeded."""
    product = LimitedProduct("Shipping", price=10, quantity=250, maximum=1)

    # Buying within the limit should work
    total_price = product.buy(1)
    assert total_price == 10
    assert product.get_quantity() == 249
    assert product.show() == "Shipping, Price: €10, Quantity: limited to 1 per order"

    # Buying more than the limit should raise an exception
    with pytest.raises(Exception, match="Cannot buy more than 1 of this item."):
        product.buy(2)  # Trying to buy more than the limit

# New tests for Promotions
def test_percent_discount_promotion():
    """Test that PercentDiscount promotion is applied correctly."""
    product = Product("MacBook Air M2", price=1450, quantity=100)
    promotion = PercentDiscount("30% off!", percent=30)
    product.set_promotion(promotion)

    # Buy 1 item, check that promotion is applied
    total_price = product.buy(1)
    assert total_price == 1015  # 30% off from 1450 is 1015

def test_second_half_price_promotion():
    """Test that SecondHalfPrice promotion is applied correctly."""
    product = Product("MacBook Air M2", price=1450, quantity=100)
    promotion = SecondHalfPrice("Second Half Price!")
    product.set_promotion(promotion)

    # Buy 2 items, check that second item is half price
    total_price = product.buy(2)
    assert total_price == 2175  # 1450 for 1st item + 725 for 2nd item

def test_third_one_free_promotion():
    """Test that ThirdOneFree promotion is applied correctly."""
    product = Product("MacBook Air M2", price=1450, quantity=100)
    promotion = ThirdOneFree("Third One Free!")
    product.set_promotion(promotion)

    # Buy 3 items, check that third item is free
    total_price = product.buy(3)
    assert total_price == 2900  # Pay for 2 items, third is free