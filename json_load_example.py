import json

json_file = 'my_file.json'
with open(json_file, 'r') as file_obj:
    my_family = json.load(file_obj)

print(my_family)
