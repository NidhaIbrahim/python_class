# A class can be derived from more than one base class - multiple inheritance
# Features of all the base classes are inherited into the derived class

class A:
    def __init__(self):
        print("from parentclass A")

    def display1(self):
        print("display1...")

    def display2(self):
        print("display2...")

    def display3(self):
        print("display3...")


class B:
    def __init__(self):
        print("from parentclass B")

    def display4(self):
        print("display4...")

# There is no relation between the classes A and B
# priority is for the left class

class C(B, A):
    def __init__(self):
        super().__init__()
        print("from derivedclass C")

    def display5(self):
        print("display5...")

object3 = C()
# print(object3.display5())
print(object3.display4())
# print(object3.display3())
# print(object3.display2())
# print(object3.display1())