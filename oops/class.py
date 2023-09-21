# class Car:
#     manufactor = "Porsche"
#     model = "456"
#     make = 2023
#     fueltype = "petrol"
#     color = "yellow"
#     price = 10000000


#     def start(self):
#         print("engine ignited")
    
#     def stop(self):
#         print("engine turned off")

#     def brake(self):
#         print(" car braked")

#     def accelerate(self):
#         print(" car is accelarating")

# car = Car()
# print(car.model)
# print(car.start())


# function add(a, b){
#     return a + b
# }

# add(10,5)
# add(20,35)

class Car:
    def __init__(self, manufactor, model, make, fueltype, color, price):
        self.manufactor_ = manufactor
        self.model_ = model
        self.make_ = make
        self.fueltype_ = fueltype
        self.color_ = color
        self.price_ = price

        # manufactor = "Porsche"
        # model = "456"
        # make = 2023
        # fueltype = "petrol"
        # color = "yellow"
        # price = 10000000


    def start(self):
        print("engine ignited")
    
    def stop(self):
        print("engine turned off")

    def brake(self):
        print(" car braked")

    def accelerate(self):
        print(" car is accelarating")

car1 = Car("Porsche", "456", 2023, "petrol", "yellow", 10000000)
car2 = Car("ferrari", "panamara", 2022, "diesel", "red", 5000000)
print(car1.model_)
print(car1.manufactor_)
# print(car1.make_)
# print(car1.fueltype_)
# print(car1.color_)
# print(car1.price_)
# print(car.accelerate())
# print(car.start())

print(car2.color_)
print(car2.manufactor_)
