"""Write Json data"""
import json
json_data={
    "id":10,
    "salary":3000,
    "Age":28
}
with open("create_json.json",mode="w") as file:
    dict_con=json.dumps(json_data)   #Dict to convert Str
    json_writer=file.write(dict_con)