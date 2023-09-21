number1 = 10
number2 = 20

print(number1 + number2)  # addition operation

str1 = "hello"
str2 = "world"

print(str1 + " " + str2) # concatination operation


str3 = "Python Programming"

print(len(str3))   #number of characters

list = [ 'python', 'react', 'flutter', 'angular' ]

print(len(list))  # number of items

user_data = {
    "name" : "fathima",
    "email" : "fathima@gmail.com",
    "contact" : 9752437823,
    "username" : "fathimas",
    "password" : "12356h"
}

print(len(user_data))  # number of keys


class Polygon:
    def render(self):
        print("rendering polygon")

class Square(Polygon):
    def render(self):
        print("rendering square")

class Circle(Polygon):
    def render(self):
        print("rendering circle")

square1 = Square()
square1.render()

circle1 = Circle()
circle1.render()
