import json

with open("create_json.json", mode="r") as file:
    json_read=file.read()
    json_con=json.loads(json_read) #Str to Convert Dict
    print(json_con)