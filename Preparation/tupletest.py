# Define the nested dictionary
divar = {"EMPID": {"DEPT": {"name": "sunil"}}}

# Define a simple function to traverse and print keys and values
def traverse_dict_simple(d):
    for key, value in d.items():
        li=[]
        li1=[]

        if isinstance(value, dict):
            li.append(key)
            li1.append(value)
            traverse_dict_simple(value)
            # Recursively call for nested dictionaries
        else:
            print(f"{key}: {value}")
    # print(li)
    print(li1)

# Traverse the dictionary
traverse_dict_simple(divar)
