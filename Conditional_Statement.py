"""if condition:
elif:
else:"""

"""@1"""
"""Lets take a strint from end user(Dynamic Data) and check Sting is Pallendrom or not"""

"""word=input("Enter Your Word")
rev=word[::-1]
if word==rev:
    print("It is a Pallendrom")
else:
    print("Not a pallendrom")"""

"""@2"""
"""Write a condition who take data end user that data divisible by 2 & 3"""

"""a=int(input('Enter a Number:'))
if a%2==0 and a%3==0:
    print(f"{a} divisible by both 3 and 4")
else:
    print(f"{a} Is not Divisible by both 3 & 4")"""


"""@3"""
"""if elif else"""

"""a=int(input('Enter a number:'))
if a%2==0 and a%3==0:
    print("Div by 2 and 3")
elif a%2==0:
    print("div only by 2")
elif a%3==0:
    print("Div only by 3")
else:
    print("Not Div by 2 & 3")"""

"""@4 H/W"""
"""if the age is <15 'Not allowed bus' >60 'Not allowed in bus'  age 15 to 25= 10 rs, age 25 to 45 =20rs , 45 to 60=30rs"""

a15to24=10
a25to44=20
a45to59=30
age=int(input("Enter Your Age"))

if age<15 or age>=60:
    print("Not Allowed in Bus")
elif age>=15 and age<25:
        print(f" {age} age is Allowed in Bus\nPrice: {a15to24} Rs ")
elif age>=25 and age<45:
        print(f" {age} age is Allowed in Bus\nPrice: {a25to44} Rs ")
elif age>=45 and age<60:
        print(f" {age} age is Allowed in Bus\nPrice: {a45to59} Rs ")

print("Thank You")