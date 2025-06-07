st = "COMBINATION"
n = len(st)
j = 0
for i in range(n):
    if i % 2 == 0:
        print(st[i:n - j])
        j += 1
    else:
        print(st[i:n - j])
        i += 1
