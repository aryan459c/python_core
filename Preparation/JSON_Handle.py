import json


""" Create JSON file"""
json_data={
    "Sunil":{
        "id":100,
        "Salary":9500,
        "Age":29
    }
}
with open("create_json.json",mode="w") as var:
    dict_con_json=json.dumps(json_data)
    json_writer=var.write(dict_con_json)

# =================================================================

with open("create_json.json",mode="r") as var:
    json_reader=var.read()   #JSON READER
    json_loads=json.loads(json_reader)  #JSON TO DICT
    print(json_loads)
    print(json_reader)
