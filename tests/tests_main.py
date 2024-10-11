import pytest

from src.main import BaseProduct, Category, LawnGrass, Product, Smartphone


def test_base_product_abstract_methods():
    with pytest.raises(TypeError) as excinfo:
        BaseProduct("test", "test", 10, 1)
    assert "Can't instantiate abstract class BaseProduct" in str(excinfo.value)


def test_product_init_and_str():
    product = Product("Product 1", "Description 1", 100.0, 5)
    assert product.name == "Product 1"
    assert product.description == "Description 1"
    assert product.price == 100.0
    assert product.quantity == 5
    assert str(product) == "Product 1, 100.0 руб. Остаток: 5 шт."


def test_product_price_setter():
    product = Product("Product 1", "Description 1", 100.0, 5)
    product.price = 150.0
    assert product.price == 150.0
    product.price = -50.0
    assert product.price == 150.0


def test_product_total_value():
    product1 = Product("Product 1", "Description 1", 100.0, 5)
    product2 = Product("Product 2", "Description 2", 200.0, 2)
    assert product1.add(product2) == 900.0


def test_smartphone_init_and_str():
    smartphone = Smartphone(
        "Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5, 95.5, "S23 Ultra", 256, "Серый"
    )
    assert smartphone.efficiency == 95.5
    assert smartphone.model == "S23 Ultra"
    assert smartphone.memory == 256
    assert smartphone.color == "Серый"
    assert "Характеристики: Эффективность: 95.5%" in str(smartphone)


def test_lawn_grass_init_and_str():
    grass = LawnGrass("Газонная трава", "Элитная трава для газона", 500.0, 20, "Россия", "7 дней", "Зеленый")
    assert grass.country == "Россия"
    assert grass.germination_period == "7 дней"
    assert grass.color == "Зеленый"
    assert "Характеристики: Страна: Россия" in str(grass)


def test_product_category_init_and_str():
    category = Category("Смартфоны", "Высокотехнологичные смартфоны")
    assert category.name == "Смартфоны"
    assert category.description == "Высокотехнологичные смартфоны"
    assert category.product_count == 0
    assert str(category) == "Смартфоны, количество продуктов: 0 шт."


def test_product_category_add_invalid_product():
    category = Category("Смартфоны", "Высокотехнологичные смартфоны")
    with pytest.raises(TypeError) as excinfo:
        category.add_product(123)
    assert "Not a product" in str(excinfo.value)


def test_product_category_middle_price():
    category = Category("Смартфоны", "Высокотехнологичные смартфоны")
    smartphone1 = Smartphone(
        "Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5, 95.5, "S23 Ultra", 256, "Серый"
    )
    smartphone2 = Smartphone("Iphone 15", "512GB, Gray space", 210000.0, 8, 98.2, "15", 512, "Gray space")
    category.add_product(smartphone1)
    category.add_product(smartphone2)
    assert category.middle_price() == 195000.0
