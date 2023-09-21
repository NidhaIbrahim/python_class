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

    def product_count(self):
        print(f"Total number of products is {Product.count}")

    def calculate_price(self):
        price = self.__price * (100 / 50)
        return price
    
    def set_price(self, price):
        self.__price = price 

    def get_price(self):
        return self.__price       


product1 = Product('pen', 'stationary', 23)


print(f"product count is {Product.count}")
print(product1.name)
print(product1.display_product())
# print(product1.__price)
print(product1.product_count())
print(product1.get_price())
print(product1.set_price(35))
print(product1.get_price())

# product2 = Product('pencil', 'stationary', 10)
# print(product2.product_count())
# print(product1.product_count())
