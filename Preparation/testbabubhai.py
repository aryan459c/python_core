lis=(["ashok", 27],["suman",30],["sunil",29],["subham",39])
lic=[]
lin=[]
def retrive():
    for i in lis:
        for j in i:
            if type(j) == str:
                lic.append(j)
            else:
                lin.append(j)
    print(lic)
    print(lin)

retrive()