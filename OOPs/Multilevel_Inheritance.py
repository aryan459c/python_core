class A:
    def f1(self):
        print("print f1")
class B(A):
    def f2(self):
        print("print f2")

class C(B):
    def f3(self):
        print("print f3")

class D(C):
    def f4(self):
        print("print f4")
obj=B()
print(obj.f2())