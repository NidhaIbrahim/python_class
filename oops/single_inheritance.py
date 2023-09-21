# ParentClass/SuperClass/BaseClass

# class ParentClass:
#     ParentClass properties

#     ParentClass functions

#  Child Class/Derived Class

# class DerivedClass(ParentClass):
#     DerivedClass properties

#     DerivedClass functions 


class A:
    def __init__(self):
        print("from parent")

    def display1(self):
        print("display1...")

    def display2(self):
        print("display2...")

    def display3(self):
        print("display3...")

object1 = A()
print(object1.display1())
print(object1.display2())
print(object1.display3())

class B(A):
    def __init__(self):
        super().__init__()
        print("from child")

    def display4(self):
        print("display4...")

object2 = B()
print(object2.display4())
print(object2.display1())
print(object2.display3())