"""
Протестируйте классы из модуля homework/models.py
"""
import pytest

from homework.models import Product, Cart


@pytest.fixture
def product():
    return Product("book", 100, "This is a book", 1000)


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