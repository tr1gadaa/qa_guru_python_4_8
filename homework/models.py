class Product:
    """
    Класс продукта
    """
    name: str
    price: float
    description: str
    quantity: int

    def __init__(self, name, price, description, quantity):
        self.name = name
        self.price = price
        self.description = description
        self.quantity = quantity

    def check_quantity(self, quantity) -> bool:
        return self.quantity >= quantity

    def buy(self, quantity):

        if self.check_quantity(quantity) is True:
            self.quantity -= quantity
            return self.quantity
        else:
            raise ValueError

    def __hash__(self):
        return hash(self.name + self.description)


class Cart:
    """
    Класс корзины. В нем хранятся продукты, которые пользователь хочет купить.
    """

    # Словарь продуктов и их количество в корзине
    products: dict[Product, int]

    def __init__(self):
        # По-умолчанию корзина пустая
        self.products = {}

    def add_product(self, product: Product, quantity=1):
        if product in self.products:
            self.products[product] += quantity
        else:
            self.products[product] = quantity
        return self.products

    def remove_product(self, product: Product, quantity=None):
        if quantity is None or quantity > self.products[product]:
            del self.products[product]
        else:
            self.products[product] -= quantity

    def clear(self):
        self.products.clear()

    def get_total_price(self, quantity=None) -> float:
        total_price = 0.0
        for product, quantity in self.products.items():
            total_price += product.price * quantity
            return total_price

    def buy(self):
        for product, quantity in self.products.items():
            if product.check_quantity(quantity):
                product.buy(quantity)
            else:
                raise ValueError("Не хватает товаров на складе")
