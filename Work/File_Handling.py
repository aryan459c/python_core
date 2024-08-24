"""read mode(r)"""
import json

file=open("demo.txt","r")
print(file.read())
print(file.read(5))

"""Write Mode"""
var=open(r"file_path","w")
var.write("Aryan")
var.writelines(["alo","rader","Ali lelo","Kanda lelo"])

"""Append mode()"""

var=open(r"file_path","a")
var.write("Water")


"""With (open or close handling)"""
with open("file path","mode") as var,open("fil_path") as var2:
    var.read()
    print(var.closed) #Check File closed or not


"""How to handel  csv and excel file"""
"""How to create csv file & insert data"""
import  csv
data_col=["id","name","age"]
data_cols=[[10,"abc",22],[11,"def",26],[12,"cba",23]]
with open("output.csv",mode="w") as file:
    csv_writer=csv.writer(file)
    csv_writer.writerow(data_col)
    csv_writer.writerows(data_cols)


"""Read CSV data"""

with open("output.csv",mode="r") as file:
    csv_reader=csv.reader(file)
    for i in csv_reader:
        print(i)


"""Handel JSON file"""
"""
DUMPS=Convert a dict to byte string(Json)
LOADS= Convert byte Sting to dict
"""

"""For Read Json"""
with open("new_data.json",mode="r") as file:
    json_reader=file.read()
    json_loads=json.loads(json_reader)

"""Write Json data"""
json_data={
    "id":10,
    "salary":3000,
    "Age":28
}
with open("create_json.json",mode="w") as file:
    dict_con=json.dumps(json_data)
    json_writer=file.write(dict_con)
