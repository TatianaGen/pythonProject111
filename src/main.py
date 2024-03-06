
from src.class_product import Product
from src.class_category import Category
from src.utils import load_data


def main():
    data = load_data()
    list_category = []
    for unit in data:
        list_product = [un for un in unit["products"]]
        category = Category(unit["name"], unit["description"], unit["products"])
        print(f'{category.get_name()}\n'
                             f'{category.get_description()}\n'
                             f'{category.get_products()}\n\n'
                             )
        result = []
        for element in list_product:
            product = Product(element["name"], element["description"],
                              element["price"], element["quantity"])
            print(f'{product.get_product_name()}\n'
                          f'{product.get_product_description()}\n'
                          f'{product.get_product_price()}\n'
                          f'{product.get_product_quantity()}\n\n'
                          )


if __name__ == '__main__':
    main()