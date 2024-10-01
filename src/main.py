from _pytest import warnings

class Product:
    def __init__(self, name: str, description: str, price: float, quantity: int):
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


class Category:
    total_categories = 0
    total_products = 0

    def __init__(self, name: str, description: str, products=None):
        if products is None:
            products = []
        self.name = name
        self.description = description
        self.__products = products if products else []
        self._update_counts()

    def _update_counts(self):
        Category.total_categories += 1
        Category.total_products += len(self.__products)

    @staticmethod
    def get_total_categories():
        return Category.total_categories

    @staticmethod
    def get_total_products():
        return Category.total_products

    def add_product(self, product: Product):
        self.__products.append(product)
        Category.total_products += 1

    @property
    def products(self):
        products_info = [
            f"{product.name}, {product.price} руб. Остаток: {product.quantity} шт."
            for product in self.__products
        ]
        return "\n".join(products_info)


if __name__ == "__main__":
    product1 = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)
    product2 = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
    product3 = Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14)

    category1 = Category(
        "Смартфоны",
        "Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для "
        "удобства жизни",
        [product1, product2, product3],
    )

    print(category1.products)
    print(f"Total categories: {Category.get_total_categories()}")
    print(f"Total products: {Category.get_total_products()}")

    product4 = Product("LG OLED 48", "4K, 120Hz", 150000.0, 4)
    category1.add_product(product4)
    print(category1.products)
    print(f"Total products: {Category.get_total_products()}")
