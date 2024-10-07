import pytest

from src.main import Category, LawnGrass, Product, Smartphone


@pytest.fixture
def product_s23_ultra():
    return Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет", 180000.0, 5)


@pytest.fixture
def iphone_15():
    return Product("Iphone 15", "512GB, Gray space", 210000.0, 8)


@pytest.fixture
def xiaomi_redmi_note_11():
    return Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14)


@pytest.fixture
def category_smartphones():
    return Category("Смартфоны", "Различные модели смартфонов")


@pytest.fixture
def smartphone_s23_ultra():
    return Smartphone("Samsung Galaxy S23 Ultra", "256GB, Серый цвет", 180000.0, 5, 95.5, "S23 Ultra", 256, "Серый")


@pytest.fixture
def iphone_15_smartphone():
    return Smartphone("Iphone 15", "512GB, Gray space", 210000.0, 8, 98.2, "15", 512, "Gray space")


@pytest.fixture
def lawn_grass():
    return LawnGrass("Газонная трава", "Элитная трава для газона", 500.0, 20, "Россия", "7 дней", "Зеленый")


def test_product_initialization(product_s23_ultra):
    assert product_s23_ultra.name == "Samsung Galaxy S23 Ultra"
    assert product_s23_ultra.description == "256GB, Серый цвет"
    assert product_s23_ultra.price == 180000.0
    assert product_s23_ultra.quantity == 5


def test_product_price_setter_positive_value(iphone_15):
    iphone_15.price = 200000.0
    assert iphone_15.price == 200000.0


def test_product_addition(product_s23_ultra, iphone_15):
    total_price = product_s23_ultra.price * product_s23_ultra.quantity + iphone_15.price * iphone_15.quantity
    assert total_price == (180000.0 * 5 + 210000.0 * 8)


def test_product_addition_invalid_type(product_s23_ultra):
    with pytest.raises(TypeError):
        _ = product_s23_ultra + 10


def test_category_initialization(product_s23_ultra, iphone_15, category_smartphones):
    category_smartphones.products = [product_s23_ultra, iphone_15]
    assert category_smartphones.name == "Смартфоны"
    assert category_smartphones.description == "Различные модели смартфонов"
    assert len(category_smartphones.products) == 2


def test_category_add_invalid_product(category_smartphones):
    with pytest.raises(TypeError):
        category_smartphones.add_product("Not a product")


def test_smartphone_initialization(smartphone_s23_ultra):
    assert smartphone_s23_ultra.name == "Samsung Galaxy S23 Ultra"
    assert smartphone_s23_ultra.efficiency == 95.5
    assert smartphone_s23_ultra.model == "S23 Ultra"
    assert smartphone_s23_ultra.memory == 256
    assert smartphone_s23_ultra.color == "Серый"


def test_lawngrass_initialization(lawn_grass):
    assert lawn_grass.name == "Газонная трава"
    assert lawn_grass.country == "Россия"
    assert lawn_grass.germination_period == "7 дней"
    assert lawn_grass.color == "Зеленый"


def test_product_addition_same_type(smartphone_s23_ultra, iphone_15_smartphone):
    total_quantity = smartphone_s23_ultra + iphone_15_smartphone
    assert total_quantity == 13


def test_product_addition_different_type(smartphone_s23_ultra, lawn_grass):
    with pytest.raises(TypeError):
        _ = smartphone_s23_ultra + lawn_grass
