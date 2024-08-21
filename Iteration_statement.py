"""
While (conditional iteration)
for (Collectional Iteration)
nested for
"""

"""Q1"""

"""li=[10,20,30,40,50]
for i in li:
    print(i)"""

"""Q2"""

"""li=[433,212,563,898,566,333,221,543,3113,67,89]
for i in li:
    i=str(i)
    if i==i[::-1]:
        print(i+" It is a pallendrom")
    else:
        print(i+" it is not a pallendrom")"""

"""Q3"""

"""li=[10,80,70,9+9j,'77','Aryan',67,89]
for i in li:
    if type(i)==str:
        print(i+"String")
    else:
        print(i)"""

"""OR"""

"""li=[10,80,70,9+9j,'77','Aryan',67,89]
for i in li:
    if isinstance(i,str):
        print(i+"String")
    else:
        print(i)"""

"""Q4"""

"""li=[1,2,[3,4]]
for i in li:
    if type(i)==list:
        for j in i:
            print(j)
    else:
        print(i)"""

"""Q5"""

"""li=[[1,2],[3,4,5],[6,7]]
for i in li:
    for j in i:
        print(j)"""

"""Q6"""

"""li=[1,2,(89,90),7,8,[90,91]]
for i in li:
    if type(i)==list or type(i)==tuple:
        for j in i:
            print(j)
    else:
            print(i)"""

"""Q7"""
"""String For loop(all char capital letter)"""

"""st="Aryan"
newst=""
for i in st:
    newst=newst+i.upper()
    print(newst)"""
"""OR"""

"""st="Aryan"
newst=""
for i in st:
    newst=i.upper()+newst
    print(newst)"""

"""Q8"""

"""st="King Kong Is GrEat"
upr=""
lor=""
for i in st:
    if i.isupper():
        upr=upr+i
        print(upr)
    else:
        if i.islower():
            lor=lor+i
            print(lor)"""

"""Q9"""

"""li = [10,24,31,43,66,87,89,21,26,90]

even_li = []
odd_li = []

for i  in li:
    if i%2==0:
        even_li.append(i)
    else:
        odd_li.append(i)
print(even_li )
print(odd_li)"""


"""Q10"""
"""pattern- *****"""

"""for i in range(5):
    print("*", end="")"""


"""Q11"""
"""
*
**
***
****
*****
"""

"""for i in range(1,6):
    print("*"*i)"""


"""Q12"""
"""
*****
****
***
**
*
"""


"""for i in range(1,6):
    print("*"*(6-i))"""


"""Q13"""
"""
     *
    **
   ***
  ****
 *****
******
"""

"""for i in range(1,7):
    print(" "*(7-(i+1))+"*"*i)"""

"""Q14"""

"""
******
 *****
  ****
   ***
    **
     *
"""

"""for i in range(1,7):
    print(" "*(i-1)+"*"*(7-i))"""