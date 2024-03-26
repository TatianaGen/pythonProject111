
from class_product import Product


class Category:
    '''
    Класс категорий товаров
    '''
    name: str
    description: str
    products = list
    category_count = 0
    products_count = 0

    def __init__(self, name, description, products):
        self.name = name
        self.description = description
        self.__products = products
        Category.category_count += 1
        Category.products_count += len(self.__products)

    def __repr__(self):
        return f'Caegory {self.name}, {self.description}, {self.__products}'

    def __len__(self):
        result = 0
        for i in self.__products:
            result += i.quantity
        return result

    def __str__(self):
        return f'{self.name}, количество продуктов: {self.__len__()} шт.'



    @property
    def products(self):
        products_list = []
        for item in self.__products:
            products_list.append(f'{item.name}, {item.price} руб. Остаток:{item.quantity} шт.')
        return products_list


    @products.setter
    def products(self, product):
        self.__products.append(product)
        if isinstance(product, Product):
            self.__products.append(product)

    @property
    def products_list(self):
        return self.__products



