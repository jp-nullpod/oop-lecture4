import json

class Dog():
    def __init__(self, name, color):
        self.name = name
        self.color = color

d = Dog("Rex", "black")

my_family = {
    "parents":['Beth', 'Jerry'],
    "children":['Summer', 'Morty']
}

my_numbers =  [12, 11, 18, 25, 36, 17]

json_file = "my_file.json"

with open(json_file, 'w') as file_obj:
    json.dump(my_numbers, file_obj, indent = 2, sort_keys=True)