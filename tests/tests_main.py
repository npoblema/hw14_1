import pytest

from src.main import Category, Product


@pytest.fixture
def product1():
    return Product("Product1", "Description1", 10.99, 5)


@pytest.fixture
def product2():
    return Product("Product2", "Description2", 20.99, 2)


@pytest.fixture
def category(product1, product2):
    return Category("Category1", "Description1", [product1, product2])


def test_product_creation(product1):
    assert product1.name == "Product1"
    assert product1.description == "Description1"
    assert product1.price == 10.99
    assert product1.quantity == 5


def test_product_count(category):
    assert Category.get_total_products() == 2


def test_category_creation(category):
    assert category.name == "Category1"
    assert category.description == "Description1"
    assert len(category.products) == 2


def test_category_count(category):
    assert Category.get_total_categories() == 3


@pytest.fixture
def other_category():
    return Category("Category2", "Description2", [])


def test_category_count_increment(other_category):
    assert Category.get_total_categories() == 4
