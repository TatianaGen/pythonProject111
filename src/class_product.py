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
        self._price = price
        self.quantity = quantity



    @classmethod
    def new_product(cls, name, description, price, quantity, products):
        cls.name = name
        cls.description = description
        cls._price = price
        cls.quantity = quantity
        if cls.name == products.name:
            cls.quantity += products.quantity
            if cls._price < products._price:
                cls._price = products._price
        return cls


    @property
    def price(self):
        return self._price
    @price.setter
    def price(self, new_price):
        if new_price < 0 or new_price == self._price:
            print('Введена некорректная цена!')
        elif new_price < self._price:
            user_answer = input('Если вы хотите поменять цену введите: y, иначе n')
            if user_answer == 'y':
                self._price = new_price
            else:
                print("Введите корректный ответ, пожалуйста!")
        else:
            self._price = new_price