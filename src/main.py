from _pytest import warnings


class Product:
    def __init__(self, name, description, price, quantity):
        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity


    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, new_price: float):
        if new_price <= 0:
            warnings.warn("Цена не должна быть нулевая или отрицательная", UserWarning)
        else:
            self.__price = new_price

    @classmethod
    def new_product(cls, product_data: dict) -> 'Product':
        return cls(
            product_data["name"],
            product_data["description"],
            product_data["price"],
            product_data["quantity"],
        )

    def __str__(self):
        return f"{self.name}, {self.price} руб. Остаток: {self.quantity} шт."

    def __add__(self, other):
        if isinstance(other, Product):
            return (self.price * self.quantity) + (other.price * other.quantity)
        return NotImplemented


class Category:
    total_categories = 0
    total_products = 0

    def __init__(self, name: str, description: str, products=None):
        if products is None:
            products = []
        self.name = name
        self.description = description
        self._products = products
        self._update_counts()

    def _update_counts(self):
        Category.total_categories += 1
        Category.total_products += len(self._products)

    @staticmethod
    def get_total_categories():
        return Category.total_categories

    @staticmethod
    def get_total_products():
        return Category.total_products

    def add_product(self, product: Product):
        self._products.append(product)
        Category.total_products += 1

    @property
    def products(self):
        return "\n".join(str(product) for product in self._products)

    def __str__(self):
        return f"{self.name}, количество продуктов: {Category.total_products} шт."

    def __add__(self, other):
        if not isinstance(other, Category):
            raise TypeError("Can only add Category objects")
        total_value = 0
        for product in self._products:
            total_value += product.price * product.quantity
        for product in other._products:
            total_value += product.price * product.quantity
        return total_value


if __name__ == '__main__':
    product1 = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)
    product2 = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
    product3 = Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14)

    print(str(product1))
    print(str(product2))
    print(str(product3))

    category1 = Category(
        "Смартфоны",
        "Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни",
        [product1, product2, product3]
    )

    print(str(category1))

    print(category1.products)

    print(product1 + product2)
    print(product1 + product3)
    print(product2 + product3)
