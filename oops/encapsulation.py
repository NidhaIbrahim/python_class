class Product:
    count = 0

    def __init__(self, name, category, price):
        self.name = name
        self.category = category
        self.price = price
        Product.count = Product.count + 1

    def display_product(self):
        print("name :", self.name)
        print("category :", self.category)
        print(f"price : {self.price}")

product1 = Product('pen', 'stationary', 23)
print(f"product count is {Product.count}")
print(product1.name)
print(product1.display_product())

product2 = Product('pencil', 'stationary', 13)
print(f"product count is {Product.count}")



