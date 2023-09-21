class Category:
    def __init__(self, category):
        self.category_ = category
    
    def get_category(self):
        return self.category_
    
class Product(Category):
    count = 0
    
    def __init__(self, name, category, price):
        super().__init__(category)
        self.name_ = name
        self.price_ = price
        Product.count = Product.count + 1

    def display_product(self):
        print(f"Product name is : {self.name_}")
        print(f"Category is : {Category.get_category(self)}")
        print(f"price of product is : {self.price_}")

    def product_count(self):
        print("Total number of products: %d" % Product.count)

product1 = Product('pen', 'stationary', '23')
print(product1.product_count())
print(product1.display_product())

