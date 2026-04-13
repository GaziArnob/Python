# import json

# py_obj = {
#     "name": "Arnob",
#     "age": 25,
#     "address": {
#         "street": "123 Main St",
#         "city": "Anytown",
#         "state": "CA",
#         "zip": "12345"
#     }
# }
# json_string = json.dumps(py_obj)
# print(json_string)  # {"name": "Arnob", "age": 25,

# json_string = '{"name": "Arnosdb", "age": 245, "address": {"stsdreet": "123 Maisdn St", "city": "Anytownsd", "state": "ad", "zip": "1234dsd5"}}'

# data = json.loads(json_string)

# print(data["name"])  # Arnob


import json

d ={
    "name": "sajid",
    "age": 30,
    "address": {
        "street": "123 Main St",
        "city": "Anytown",
        "state": "CA",
        "zip": "12345"
    }
}


with open("data.json", "w") as file:
    json.dump(d, file, indent=4 ,sort_keys=True)



