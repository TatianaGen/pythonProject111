from abc import ABC, abstractmethod
from mixin import MixinShow

class BaseProduct(ABC):
    """
     Абстрактный класс товаров
    """

    @abstractmethod
    def __str__(self):
        pass


class Product(BaseProduct, MixinShow):
    """
     Класс товаров
    """
    def __init__(self, name, description, price, quantity):
        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity
        super().__init__()

    def __repr__(self):
        return f'Product {self.name}, {self.description}, {self.__price}, {self.quantity}'

    def __str__(self):
        return f'{self.name}, {self.__price} руб. Остаток: {self.quantity} шт.'


    def __add__(self, other):
        result = (self.__price * self.quantity) + (other.__price * other.quantity)
        return result
        if type(self) == type(other):
            result = (self.__price * self.quantity) + (other.__price * other.quantity)
            return result
        else:
            raise TypeError('Можно складывать только экземпляры одного и того же класса!')


    @classmethod
    def new_product(cls, name, description, price, quantity):
        return cls(name, description, price, quantity)


    @property
    def price(self):
        return self.__price
    @price.setter
    def price(self, new_price):
        if new_price < 0 or new_price == self.__price:
            print('Введена некорректная цена!')
        elif new_price < self._price:
            user_answer = input('Если вы хотите поменять цену введите: y, иначе n')
            if user_answer == 'y':
                self.__price = new_price
            else:
                print("Введите корректный ответ, пожалуйста!")
        else:
            self._price = new_price


class SmartPhone(Product, MixinShow):
    def __init__(self, name, description, price, quantity, performance, model, memory, color):
        super().__init__(name, description, price, quantity)
        self.performance = performance
        self.model = model
        self.memory = memory
        self.color = color



class LawnGrass(Product, MixinShow):
    def __init__(self, name, description, price, quantity, manufacturer, germination, color):
        super().__init__(name, description, price, quantity)
        self.manufacturer = manufacturer
        self.germination = germination
        self.color = color

