def decor_result(res_func):
    def distinction(marks):
        for m in marks:
            if m>=75:
                print("Distinction")
            else:
                res_func(marks)
    return distinction
@decor_result
def result(marks):
    for m in marks:
        if m>33:
            pass
        else:
            print("Fail")
            break
    else:
        print("Pass")
result([55,26,45,80,45])