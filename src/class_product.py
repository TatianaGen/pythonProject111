class Product:
    name: str
    description: str
    price: str
    quantity: int

    def __init__(self, name, description, price, quantity):
        self.name = name
        self.description = description
        self.price = price
        self.quantity = quantity

    def get_product_name(self):
        return self.name

    def get_product_description(self):
        return self.description

    def get_product_price(self):
        return self.price

    def get_product_quantity(self):
        return self.quantity