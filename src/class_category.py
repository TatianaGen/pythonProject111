class Category:
    name: str
    description: str
    products: str

    category_count = 0
    products_count = 0

    def __init__(self, name, description, products):
        self.name = name
        self.description = description
        self.products = products

        Category.category_count += 1
        Category.products_count += len(self.products)


    def get_name(self):
        return self.name

    def get_description(self):
        return self.description

    def get_products(self):
        return self.products