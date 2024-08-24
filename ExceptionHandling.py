try:
    num1=int(input("First Num"))
    num2 = int(input("Second Num"))
    div=num1//num2
    print(div)
except ZeroDivisionError as msg:
    print(f"Try to put Without zero:- {msg}")
except Exception as e:
    print(e)