import pytest
from src.class_category import Category
from src.class_product import Product


@pytest.fixture
def class_category():
    return Category('Смартфоны',
                    'Смартфоны, как средство не только коммуникации, но и получение дополнительных функций для удобства жизни',
                    {
                        "name": "Samsung Galaxy C23 Ultra",
                        "description": "256GB, Серый цвет, 200MP камера",
                        "price": 180000.0,
                        "quantity": 5
                    })


def test_category_init(class_category):
    assert class_category.name == 'Смартфоны'
    assert class_category.description == 'Смартфоны, как средство не только коммуникации, но и получение дополнительных функций для удобства жизни'
    assert class_category.products == {'description': '256GB, Серый цвет, 200MP камера',
                                       'name': 'Samsung Galaxy C23 Ultra',
                                       'price': 180000.0,
                                       'quantity': 5}

    assert class_category.category_count == 1
    assert Category.products_count == 4


def test_get_name(class_category):
    class_category.get_name()
    assert class_category.get_name() == 'Смартфоны'


def test_get_description(class_category):
    class_category.get_description()
    assert class_category.get_description() == 'Смартфоны, как средство не только коммуникации, но и получение дополнительных функций для удобства жизни'


def test_get_products(class_category):
    class_category.get_products()
    assert class_category.get_products() == {
        "name": "Samsung Galaxy C23 Ultra",
        "description": "256GB, Серый цвет, 200MP камера",
        "price": 180000.0,
        "quantity": 5
    }


@pytest.fixture
def class_product():
    return Product("Samsung Galaxy C23 Ultra", "256GB, Серый цвет, 200MP камера",
                   180000.0, 5)


def test_product_init(class_product):
    assert class_product.name == 'Samsung Galaxy C23 Ultra'
    assert class_product.description == '256GB, Серый цвет, 200MP камера'
    assert class_product.price == 180000.0
    assert class_product.quantity == 5


def test_product_name(class_product):
    class_product.get_product_name()
    assert class_product.get_product_name() == 'Samsung Galaxy C23 Ultra'


def test_product_description(class_product):
    class_product.get_product_description()
    assert class_product.get_product_description() == '256GB, Серый цвет, 200MP камера'


def test_product_price(class_product):
    class_product.get_product_price()
    assert class_product.get_product_price() == 180000.0


def test_product_quantity(class_product):
    class_product.get_product_quantity()
    assert class_product.get_product_quantity == 5