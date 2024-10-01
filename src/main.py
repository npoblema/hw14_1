from _pytest import warnings


class Product:
    def __init__(self, name: str, description: str, price: float, quantity: int):
        self.name = name
        self.description = description
        self._price = price # Приватный атрибут для цены
        self.quantity = quantity

    @property
    def price(self):
        """Геттер для атрибута цены."""
        return self._price

    @price.setter
    def price(self, new_price: float):
        """Сеттер для атрибута цены с проверкой."""
        if new_price <= 0:
            warnings.warn("Цена не должна быть нулевая или отрицательная", UserWarning)
        else:
            self._price = new_price

    @classmethod
    def new_product(cls, product_data: dict) -> 'Product':
        """
        Создает новый объект Product из словаря данных.
        """
        return cls(
            product_data["name"],
            product_data["description"],
            product_data["price"],
            product_data["quantity"],
        )


class Category:
    def __init__(self, name: str, description: str, products=None):
        if products is None:
            products = []
        self.name = name
        self.description = description
        self._products = products # Приватный атрибут для списка товаров
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
        """
        Добавляет продукт в список товаров категории.
        """
        self._products.append(product)

    @property
    def products(self):
        """
        Геттер для вывода списка товаров в виде строк.
        """
        products_info = [
            f"{product.name}, {product.price} руб. Остаток: {product.quantity} шт."
            for product in self._products
        ]
        return "\n".join(products_info)

Category.total_categories = 0
Category.total_products = 0

if __name__ == "__main__":
    product1 = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)
    product2 = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
    product3 = Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14)

    print(product2.name)
    print(product2.description)
    print(product2.price) # Используем геттер price для доступа к цене
    print(product2.quantity)

    print(product1.name)
    print(product1.description)
    print(product1.price)
    print(product1.quantity)

    print(product3.name)
    print(product3.description)
    print(product3.price)
    print(product3.quantity)

    category1 = Category(
        "Смартфоны",
        "Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для "
        "удобства жизни",
        [product1, product2, product3],
    )

    print(category1.name == "Смартфоны")
    print(category1.description)
    print(category1.products) # Используем products как свойство для вывода
    print(Category.get_total_categories())
    print(Category.get_total_products())

    product4 = Product('55" QLED 4K', "Фоновая подсветка", 123000.0, 7)
    category2 = Category(
        "Телевизоры",
        "Современный телевизор, который позволяет наслаждаться просмотром, станет вашим другом и "
        "помощником",
        [product4],
    )

    print(category2.name)
    print(category2.description)
    print(category2.products)
    print(Category.get_total_categories())
    print(Category.get_total_products())

    # Добавляем новый продукт в категорию "Телевизоры" через метод add_product
    category2.add_product(Product("LG OLED 48", "4K, 120Hz", 150000.0, 4))
    print(category2.products)

    # Создаем новый продукт из словаря с помощью класс-метода new_product
    new_product_data = {
        "name": "Samsung Galaxy S24",
        "description": "512GB, Черный цвет, 200MP камера",
        "price": 200000.0,
        "quantity": 3
    }
    new_product = Product.new_product(new_product_data)
    print(f"Созданный продукт: {new_product.name}, {new_product.price} руб., {new_product.quantity} шт.")

    # Добавляем новый продукт в категорию "Смартфоны"
    category1.add_product(new_product)
    print(category1.products)

    # Пробуем изменить цену на отрицательное значение
    product1.price = -100
    print(product1.price) # Цена не изменится, т.к. выведено предупреждение
