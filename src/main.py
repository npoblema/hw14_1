from _pytest import warnings

class Product:
    def __init__(self, name, description, price, quantity):
        self.name = name
        self.description = description
        self.price = price
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

class Smartphone(Product):
    def __init__(self, name, description, price, quantity, efficiency, model, memory, color):
        super().__init__(name, description, price, quantity)
        self.efficiency = efficiency
        self.model = model
        self.memory = memory
        self.color = color

class LawnGrass(Product):
    def __init__(self, name, description, price, quantity, country, germination_period, color):
        super().__init__(name, description, price, quantity)
        self.country = country
        self.germination_period = germination_period
        self.color = color

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

    def add_product(self, product):
        if not isinstance(product, Product) or not issubclass(type(product), Product):
            raise TypeError("Only Product objects or its subclasses can be added")
        self._products.append(product)
        Category.total_products += 1

    @property
    def products(self):
        return "\n".join(str(product) for product in self._products)

    def __str__(self):
        return f"{self.name}, количество продуктов: {len(self._products)} шт."

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
    smartphone1 = Smartphone("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5, "High", "S23 Ultra", "256GB", "Gray")
    smartphone2 = Smartphone("Iphone 15", "512GB, Gray space", 210000.0, 8, "Very High", "15 Pro Max", "512GB", "Space Gray")
    smartphone3 = Smartphone("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14, "Medium", "Note 11 Pro", "1024GB", "Blue")

    lawn_grass1 = LawnGrass("Газонная трава 'Изумруд'", "Для газонов", 100.0, 10, "Россия", 7, "Зеленый")
    lawn_grass2 = LawnGrass("Газонная трава 'Росинка'", "Для газонов", 150.0, 5, "Россия", 10, "Зеленый")

    category_smartphones = Category("Смартфоны", "Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни", [smartphone1, smartphone2, smartphone3])
    category_lawn_grass = Category("Газонная трава", "Газонная трава для красивого газона", [lawn_grass1, lawn_grass2])

    print(category_smartphones.products)
    print(category_lawn_grass.products)

    print(category_smartphones + category_lawn_grass)

    try:
        result_smartphone = smartphone1 + smartphone2
        print(f"Сложение смартфонов: {result_smartphone}")
    except TypeError as e:
        print(f"Ошибка сложения: {e}")

    try:
        result_mixed = smartphone1 + lawn_grass1
        print(f"Сложение смартфона и травы: {result_mixed}")
    except TypeError as e:
        print(f"Ошибка сложения: {e}")
