import pytest
from src.main import Product, Category

class TestProduct:
    def test_new_product(self):
        product_data = {
            "name": "Samsung Galaxy S24",
            "description": "512GB, Черный цвет, 200MP камера",
            "price": 200000.0,
            "quantity": 3
        }
        new_product = Product.new_product(product_data)
        assert new_product.name == "Samsung Galaxy S24"
        assert new_product.description == "512GB, Черный цвет, 200MP камера"
        assert new_product.price == 200000.0
        assert new_product.quantity == 3

    def test_price_getter(self):
        product = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
        assert product.price == 210000.0

    def test_price_setter_valid(self):
        product = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
        product.price = 250000.0 # Новая корректная цена
        assert product.price == 250000.0

    def test_price_setter_invalid(self):
        product = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
        with pytest.warns(UserWarning) as record:
            product.price = 0
        assert len(record) == 1
        assert "Цена не должна быть нулевая или отрицательная" in str(record[0].message)
        assert product.price == 210000.0 # Цена не должна измениться

    def test_price_setter_negative(self):
        product = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
        with pytest.warns(UserWarning) as record:
            product.price = -100
        assert len(record) == 1
        assert "Цена не должна быть нулевая или отрицательная" in str(record[0].message)
        assert product.price == 210000.0

class TestCategory:
    def test_category_creation(self):
        product1 = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)
        product2 = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
        category1 = Category("Смартфоны", "Описание смартфонов", [product1, product2])
        assert category1.name == "Смартфоны"
        assert category1.description == "Описание смартфонов"
        assert category1.products == "Samsung Galaxy S23 Ultra, 180000.0 руб. Остаток: 5 шт.\nIphone 15, 210000.0 руб. Остаток: 8 шт."
        assert Category.get_total_categories() == 1
        assert Category.get_total_products() == 2

    def test_add_product(self):
        category1 = Category("Смартфоны", "Описание смартфонов")
        product3 = Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14)
        category1.add_product(product3)
        assert category1.products == "Xiaomi Redmi Note 11, 31000.0 руб. Остаток: 14 шт."
        assert Category.get_total_products() == 1

    def test_products_getter(self):
        product1 = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)
        product2 = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
        category1 = Category("Смартфоны", "Описание смартфонов", [product1, product2])
        assert category1.products == "Samsung Galaxy S23 Ultra, 180000.0 руб. Остаток: 5 шт.\nIphone 15, 210000.0 руб. Остаток: 8 шт."

    def test_total_categories_and_products(self):
        assert Category.get_total_categories() == 0
        assert Category.get_total_products() == 0
