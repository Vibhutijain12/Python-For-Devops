## 1. write a python script which reads an APIs and parse a JSON and stores the output in json file.

import requests
import json

response = requests.get("https://dummyjson.com/todos")
data = response.json()

for key, value in data["todos"][0].items():  # Accessing the first todo item
    print(f"{key}: {value}")

# print("-----")

# print(type(data["todos"]))

for todo in data["todos"]:      ## Looping through each todo item
    for key, value in todo.items():
        print(f"{key}: {value}")
    print("-----")


filename = "todos.json" 
with open(filename, 'w') as file: 
    json.dump(data, file, indent=4)

print(f"Data has been written to {filename}")
