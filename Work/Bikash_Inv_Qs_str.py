var1 = "This is a coding test, All the best"


def revers_str(str1):
    return str1[::-1]


var1 = var1.split(',')
var2 = var1[0].split(' ')
var3 = []
var4 = var1[1].split(' ')
num = 0

for i in var2:
    if num == 0:
        var3.append(revers_str(var2[num]))
    elif num == 3:
        var3.append(revers_str(var2[num]))
    else:
        var3.append(var2[num])
    num += 1

var1_second_part = var1[1].split(' ')
var1_second_part[2] = revers_str(var1_second_part[2])
main_var = ' '.join(var3) + ',' + ' '.join(var1_second_part)
print(main_var)
