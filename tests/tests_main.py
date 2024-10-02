import pytest

from src.main import Product, Category

def test_product_str():
    product = Product("Телефон", "Описание", 100.0, 5)
    assert str(product) == "Телефон, 100.0 руб. Остаток: 5 шт."

def test_category_str():
    product_a = Product("Телефон", "Описание", 100.0, 5)
    product_b = Product("Планшет", "Описание", 200.0, 10)
    category = Category("Электроника", "Описание", [product_a, product_b])
    assert str(category) == "Электроника, количество продуктов: 2 шт."

def test_category_add():
    product_a = Product("Телефон", "Описание", 100.0, 5)
    product_b = Product("Планшет", "Описание", 200.0, 10)
    category1 = Category("Электроника", "Описание", [product_a, product_b])
    product_c = Product("Ноутбук", "Описание", 300.0, 2)
    category2 = Category("Компьютеры", "Описание", [product_c])
    assert category1 + category2 == 100 * 5 + 200 * 10 + 300 * 2

def test_category_products():
    product_a = Product("Телефон", "Описание", 100.0, 5)
    product_b = Product("Планшет", "Описание", 200.0, 10)
    category = Category("Электроника", "Описание", [product_a, product_b])
    assert category.products == "Телефон, 100.0 руб. Остаток: 5 шт.\nПланшет, 200.0 руб. Остаток: 10 шт."

def test_category_add_invalid_type():
    product_a = Product("Телефон", "Описание", 100.0, 5)
    product_b = Product("Планшет", "Описание", 200.0, 10)
    category1 = Category("Электроника", "Описание", [product_a, product_b])
    with pytest.raises(TypeError):
        category1 + "invalid"
