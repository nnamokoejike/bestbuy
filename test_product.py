import pytest
from products import Product # Replace 'your_module' with the actual module name where your Product class is defined

def test_create_normal_product():
    product = Product(name="Example Product", price=10.0, quantity=20)
    assert product.name == "Example Product"
    assert product.price == 10.0
    assert product.quantity == 20
    assert product.is_active()

def test_create_product_with_invalid_details_empty_name():
    with pytest.raises(ValueError, match="Invalid input. Please provide valid input"):
        Product(name="", price=1450, quantity=100)

def test_create_product_with_invalid_details_negative_price():
    with pytest.raises(ValueError, match="Invalid input. Please provide valid input"):
        Product(name="MacBook Air M2", price=-10, quantity=100)

def test_zero_quantity_deactivates_product():
    product = Product(name="Example Product", price=10.0, quantity=0)
    assert not product.is_active()

def test_product_purchase_modifies_quantity_and_returns_output():
    product = Product(name="Example Product", price=10.0, quantity=20)
    total_price = product.buy(5)
    assert product.quantity == 15
    assert total_price == 50.0

def test_buying_larger_quantity_than_exists_raises_exception():
    product = Product(name="Example Product", price=10.0, quantity=20)
    with pytest.raises(ValueError, match="Insufficient quantity of Example Product available."):
        product.buy(25)


