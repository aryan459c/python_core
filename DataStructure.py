"""LIST AND TUPLE"""
"""list"""
a=[1,2,3,12.3,24+3j,'table']
print(type(a))

"""List append()"""
a.append('ok')
a.append("top")
print(a)

"""insert(indexno,Object)"""
a.insert(4,236)
print(a)


"""list1.extend(list2)"""
b=[20,30,50]
c=[80,90,40]
b.extend(c)
print(b)

"""li.clear()"""
b.clear()
print(b)

"""li.pop()"""
b=[20,30,40,50]
b.pop(1)
print(b)

"""li.remove(30)"""

# b.remove(30)
# print(b)

"""li.count()"""

d=[10,20,40,20,36,20]
e=d.count(20)
print(e)

