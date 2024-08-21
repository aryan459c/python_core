def calcu(*args):

    result = 0
    for i in args:
        arth = input(f'Enter your operation [{result}__{i}]:-')
        if arth=="+":
            result = result+i
        elif arth=="-":
            result = result-i
        elif arth=="*":
            result = result*i
        elif arth=="/":
            result = result//i
    return result

print(calcu(10,20,30))