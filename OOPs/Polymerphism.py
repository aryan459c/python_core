"""When Class have a 4 same method then python take last one and all method garbaged"""
"1. Method Overloading 2. Method OverRidding"

"""OVERLOADING"""
"""class A:
    def f1(self):
        print("f1 0")

    def f1(self):
        print("f1 1")

obj=A()
print(obj.f1())"""


# ================================================================

"""Method OverRidding"""
class Parent:
    def show_message(self):
        print("Message from Parent")

class Child(Parent):
    def show_message(self):
        print("Message from Child")

# Create objects
parent = Parent()
child = Child()

# Call methods
parent.show_message()  # Output: Message from Parent
child.show_message()   # Output: Message from Child
