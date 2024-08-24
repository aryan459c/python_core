"""Filter"""
from functools import reduce

li=[10,23,45,32,67,89,76,65,221,41]
var=list(filter(lambda n:n%2==0,li))
print(var)

"""Map()"""
li1=[10,23,46,89,79]
var2=list(map(lambda n:n+1,li))
print(var2)

"""reduce"""
li3=[10,23,46,89,78]
var3=reduce(lambda a,b:a+b,li)
print(var3)