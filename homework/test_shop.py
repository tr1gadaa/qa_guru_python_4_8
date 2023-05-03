"""
Протестируйте классы из модуля homework/models.py
"""
import pytest

from homework.models import Product, Cart


@pytest.fixture
def product():
    return Product("book", 100, "This is a book", 1000)

@pytest.fixture
def cart(product):
    return Cart()

class TestProducts:

    def test_product_check_quantity(self, product):
        assert product.check_quantity(product.quantity)
        assert not product.check_quantity(1001)


    def test_product_buy(self, product):
        product.buy(product.quantity)
        assert product.quantity == 0


    def test_product_buy_more_than_available(self, product):
        with pytest.raises(ValueError, match="Вы хотите купить слишком много"):
            product.buy(1001)


class TestCart:
    """
    TODO Напишите тесты на методы класса Cart
        На каждый метод у вас должен получиться отдельный тест
        На некоторые методы у вас может быть несколько тестов.
        Например, негативные тесты, ожидающие ошибку (используйте pytest.raises, чтобы проверить это)
    """

    def test_add_product(self, cart, product):
        cart.add_product(product, 999)
        assert cart.products[product] == 999

    def test_add_product_twice(self, cart, product):
        cart.add_product(product, 1)
        cart.add_product(product, 100)
        assert cart.products[product] == 101

    def test_remove_product_from_cart(self, cart, product):
        cart.add_product(product, 101)
        cart.remove_product(product, 1)
        assert cart.products[product] == 100

    def test_remove_all_product_from_cart(self, cart, product):
        cart.add_product(product, 101)
        cart.remove_product(product, 102)
        assert cart.products[product] == 0
