list=[9,26,7,6,30,56,25]

for i in range(len(list)):
    for j in range(0, len(list)-i-1):
        if list[j]>list[j+1]:
            list[j],list[j + 1]=list[j + 1],list[j]

print(list)
