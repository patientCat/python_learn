import json
from dataclasses import dataclass

# Define a data class
@dataclass
class Person:
    def __init__(self, Name, age):
        self.name = Name
        self.age = age

# JSON string
json_str = '{"Name": "John", "age": 30}'

# Convert JSON string to a dictionary
json_dict = json.loads(json_str)

# Convert dictionary to a data class instance
person = Person(**json_dict)

# Access data class attributes
print(person.name)  # Output: John
print(person.age)   # Output: 30

person.name = "luke"
print(person.name)  # Output: luke


import types

# Create a SimpleNamespace object
ns = types.SimpleNamespace()

# Set attributes
ns.name = "John"
ns.age = 30

# Access attributes
print(ns.name)  # Output: John
print(ns.age)   # Output: 30

# Delete an attribute
del ns.age

# Check if an attribute exists
if hasattr(ns, "age"):
    print("Age attribute exists.")
else:
    print("Age attribute does not exist.")

# JSON string
json_str = '{"name": "John", "age": 30, "list":[{"name":"dog", "type":1}]}'

# Convert JSON string to a dictionary
ns = json.loads(json_str, object_hook=lambda d: types.SimpleNamespace(**d))

print(ns.list)
print(ns.list[0].name)
