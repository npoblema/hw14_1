from abc import ABC, abstractmethod


class AbstractProduct(ABC):
    @abstractmethod
    def __init__(self, name, description, price, quantity):
        self.name = name
        self.description = description
        self._price = price
        self.quantity = quantity

    @abstractmethod
    def __str__(self):
        pass


class LoggerMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        print(f"Создан объект класса {self.__class__.__name__} с параметрами: {args}")


class Product(LoggerMixin, AbstractProduct):
    product_count = 0

    def __init__(self, name, description, price, quantity):
        super().__init__(name, description, price, quantity)
        Product.product_count += 1

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, new_price):
        if new_price > 0:
            self._price = new_price
        else:
            print("Цена должна быть положительной")

    def __str__(self):
        return f"{self.name}: {self.price:.2f} руб. Остаток: {self.quantity} шт."

    def total_value(self):
        return self.price * self.quantity


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


class ProductCategory:
    def __init__(self, name, description, products=None):
        self.name = name
        self.description = description
        self.products = products if products is not None else []

    def add_product(self, product):
        if isinstance(product, Product):
            self.products.append(product)
        else:
            raise TypeError("Только продукты могут быть добавлены")

    @property
    def total_product_count(self):
        return sum(product.quantity for product in self.products)

    def __str__(self):
        return f"{self.name}: {self.total_product_count} продуктов"


if __name__ == "__main__":
    smartphone1 = Smartphone(
        "Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5, 95.5, "S23 Ultra", 256, "Серый"
    )
    smartphone2 = Smartphone("Iphone 15", "512GB, Gray space", 210000.0, 8, 98.2, "15", 512, "Gray space")
    grass1 = LawnGrass("Газонная трава", "Элитная трава для газона", 500.0, 20, "Россия", "7 дней", "Зеленый")

    smartphone_category = ProductCategory("Смартфоны", "Высокотехнологичные смартфоны", [smartphone1, smartphone2])
    grass_category = ProductCategory("Газонная трава", "Различные виды газонной травы", [grass1])

    print("\nКатегории:")
    print(smartphone_category)
    print(grass_category)

    try:
        smartphone_category.add_product("Not a product")
    except TypeError as e:
        print(f"Ошибка: {e}")

    print("\nСложение товаров:")
    smartphone_sum = smartphone1.total_value() + smartphone2.total_value()
    print(f"Стоимость всех смартфонов: {smartphone_sum:.2f}")
