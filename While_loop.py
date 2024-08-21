"""Write a pallendrom Number with help of while loop without using string"""
num =int(input("Enter a number:- "))
orginal_num = num
rev_num = 0

while num > 0:
    digit = num % 10
    rev_num = rev_num * 10+ digit
    num = num // 10
if orginal_num == rev_num:
    print(f"{orginal_num} is a palindrome.")
else:
    print(f"{orginal_num} is not a palindrome.")