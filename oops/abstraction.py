# access modifiers/specifiers are used to implement concept of data hiding.
# To make an entity private prefix the name with double underscore(__)

class Product:
    count = 0

    def __init__(self, name, category, price):
        self.name = name
        self.category = category
        self.__price = price
        Product.count = Product.count + 1

    def display_product(self):
        print("name :", self.name)
        print("category :", self.category)
        print(f"price : {self.__price}")

product1 = Product('pen', 'stationary', 23)
print(f"product count is {Product.count}")
print(product1.name)
# print(product1.__price)
print(product1.category)
print(product1.display_product())

product2 = Product('pencil', 'stationary', 13)
print(f"product count is {Product.count}")



