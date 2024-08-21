li = [
{'Name':'A','Age':26,'Salary':67000},
{'Name':'B','Age':27,'Salary':89000},
{'Name':'C','Age':34,'Salary':65000},
{'Name':'D','Age':33,'Salary':72000},
{'Name':'E','Age':37,'Salary':60000},
{'Name':'F','Age':33,'Salary':72000},
{'Name':'G','Age':33,'Salary':72000},
{'Name':'G','Age':33,'Salary':70000},

]


"""for  i in li:
    if i['Age']>30:
        print(i["Name"],i["Age"])"""

"""for i in li:
        if i.get('Age')>30:
            print(i["Name"])
            print(i['Age'])"""


"""for i in li:
        if i.get('Salary')>60000 and i.get('Salary')<70000:
            print(i["Name"])
            print(i['Age'])"""


"""for i in li:
    if 60000 <= i['Salary'] <= 70000:
        print(i['Name'], i['Age'])"""

"""
li = [
{'Name':'A','Age':26,'Salary':67000,'Subjcet':['Python','Java ','C']},
{'Name':'B','Age':27,'Salary':89000,'Subjcet':['Ruby','Golang ','C']},
{'Name':'C','Age':34,'Salary':65000,'Subjcet':['.Net','SQL ','Perl']},
{'Name':'D','Age':33,'Salary':72000,'Subjcet':['Python','Perl ','Ruby']},
{'Name':'E','Age':38,'Salary':60000,'Subjcet':['SQL','Java ','PLSQL']},
]
for i in li:
    if 'Python' in i['Subjcet']:
            print(i['Name'])

"""

"""num = 1
num_end = 10
sum = 0
while num <= num_end:
    sum += num
    num += 1
    print(num)
print(sum)"""