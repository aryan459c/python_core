class Alg:
    def __init__(self,a,b):
        self.a=a
        self.b=b
    def addtion(self):
        result=self.a+self.b
        return result
    def multiplication(self):
        result=self.a*self.b*self.addtion()
        return result
    def division(self):
        result=self.multiplication()/self.addtion()
        return result
obj=Alg(10,20)
print(obj.addtion())
print(obj.multiplication())
print(obj.division())