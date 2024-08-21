"""CAPITALIZE"""
a='jryan of right'
print(a.capitalize())

"""count"""
print(a.count('a'))

"""strip"""
a="   aryan   "
print("Split:"+a.strip())
a="====Aryan==="
print("Lsplit:"+a.lstrip("="))
a="====Aryan==="
print("Rsplit:"+a.rstrip("="))



b="Company30"
print(b.isalnum())
c="CUNIL"
print(c.isupper())

"""SPLIT"""
name='Hello world this is python'
print(name.split())

"""REPLACE()"""
print(name.replace("Hello","noty"))

"""JOIN"""
li=['Hello', 'world', 'this', 'is', 'python']
li=" ".join(li)
li1="".join(li)
print('Convert String with space:'+li)
print(" convert String:"+li1)

"""FIND AND INDEX"""
a='Aryan'
print(a.find('y'))
print(a.index('y'))

"""FORMAT STRING METHODE"""
a=30
print(f"a value is :{a}")