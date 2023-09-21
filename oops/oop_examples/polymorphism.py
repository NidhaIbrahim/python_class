class Product:
    count = 0

    def __init__(self, name, category, price):
        self.name = name
        self.category = category
        self.price = price
        Product.count = Product.count + 1

    def display_product(self):
        print(f"Product name is : {self.name}")
        print(f"Category is : {self.category}")
        print(f"price of product is : {self.price}")

    def display(self):
        print(f"Total number of products : {Product.count}")

    def calculate_price(self):
        price = self.price + 20
        return price
    

class Sales(Product):
    def __init__(self, name, category, price, qty):
        Product.__init__(self, name, category, price)
        self.qty = qty

    def calculate_price(self):
        total = Product.calculate_price(self) * self.qty
        return total
    
sales1 = Sales('pen', 'stationary', 10, 3)
prod1 = Product('pen', 'stationary', 10)
print(sales1.calculate_price()) # gives 90
print(prod1.calculate_price())  # gives 30