"""li=[10,20,[78,90],(45,91)]
new_li = [j for i in li  for j in (i if isinstance(i,(list,tuple)) else [i])]
print(new_li)"""
from faker import Faker
fake= Faker()
i=0
while i<4:
    var=fake.name()
    if var.startswith('S'):
        print(var)
        i+=1

