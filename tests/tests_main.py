import pytest
from src.main import Product, Smartphone, LawnGrass, ProductCategory


def test_product_initialization():
    product = Product("Товар", "Описание товара", 100.0, 10)
    assert product.name == "Товар"
    assert product.description == "Описание товара"
    assert product.price == 100.0
    assert product.quantity == 10


def test_product_price_setter():
    product = Product("Товар", "Описание товара", 100.0, 10)
    product.price = 120.0
    assert product.price == 120.0

    product.price = -50.0
    assert product.price == 120.0


def test_product_str():
    product = Product("Товар", "Описание товара", 100.0, 10)
    assert str(product) == "Товар: 100.00 руб. Остаток: 10 шт."


def test_smartphone_initialization():
    smartphone = Smartphone("iPhone", "Смартфон от Apple", 999.0, 5, 98.2, "13", 256, "Черный")
    assert smartphone.name == "iPhone"
    assert smartphone.model == "13"


def test_lawn_grass_initialization():
    grass = LawnGrass("Газонная трава", "Элитная трава для газона", 500.0, 20, "США", "10 дней", "Зеленый")
    assert grass.country == "США"
    assert grass.germination_period == "10 дней"


def test_product_category_initialization():
    category = ProductCategory("Смартфоны", "Различные смартфоны")
    assert category.name == "Смартфоны"
    assert category.description == "Различные смартфоны"
    assert category.products == []


def test_add_product_to_category():
    category = ProductCategory("Смартфоны", "Различные смартфоны")
    smartphone = Smartphone("Samsung Galaxy", "Смартфон", 700.0, 5, 95.5, "Galaxy", 128, "Синий")

    category.add_product(smartphone)
    assert smartphone in category.products
    assert category.total_product_count == 5


def test_add_non_product_to_category():
    category = ProductCategory("Смартфоны", "Различные смартфоны")
    with pytest.raises(TypeError, match="Только продукты могут быть добавлены"):
        category.add_product("Not a product")


def test_product_sum_value():
    smartphone1 = Smartphone("Samsung Galaxy", "Смартфон", 700.0, 5, 95.5, "Galaxy", 128, "Синий")
    smartphone2 = Smartphone("iPhone", "Смартфон", 999.0, 3, 98.2, "13", 256, "Черный")

    total_value = smartphone1.total_value() + smartphone2.total_value()
    assert total_value == (700.0 * 5) + (999.0 * 3)


if __name__ == "__main__":
    pytest.main()
