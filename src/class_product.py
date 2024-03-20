class Product:
    """
     Класс товаров
    """
    name: str
    description: str
    price: float
    def __init__(self, name, description, price, quantity):
        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity

    def __repr__(self):
        return f'Product {self.name}, {self.description}, {self.__price}, {self.quantity}'

    def __str__(self):
        return f'{self.name}, {self.price} руб. Остаток: {self.quantity} шт.'


    def __add__(self, other):
        return (self.price * self.quantity) + (other.price * other.quantity)

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
                self._price = new_price
            else:
                print("Введите корректный ответ, пожалуйста!")
        else:
            self._price = new_price
