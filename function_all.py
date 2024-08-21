"""def is_armstr_num(number) :
    num_str = str(number)
    num_len = len(num_str)
    sop = 0     #Sum Of Power
    for digit in num_str:
        sop += int(digit) ** num_len
    if sop == number:
        return (f"{number} is an Armstrong number.")
    else:
        return(f"{number} is not an Armstrong number.")

print(is_armstr_num(int(input("Enter a number"))))"""


"""def is_armstr_num(number) :
    str_len= len(str(number))
    sop = 0  # Sum Of Power
    temp = number
    while temp>0:
        digit = temp % 10
        sop += int(digit) ** str_len
        temp //= 10
    if sop == number:
        return (f"{number} is an Armstrong number.")
    else:
        return(f"{number} is not an Armstrong number.")

print(is_armstr_num(int(input("Enter a number"))))"""
