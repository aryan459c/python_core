def ex_recursion(num):
    if num == 1:
        return 1
    else:
        return num * ex_recursion(num-1)
print(ex_recursion(4))
