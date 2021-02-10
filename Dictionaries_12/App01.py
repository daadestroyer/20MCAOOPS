mydict = {
    "brand":"Ford",
    "model":"Mustang",
    "year":1964, 
    "year":2020  # duplicates values will override
}

print(mydict)

# Getting keys
print(mydict.keys())

# Getting values

print(mydict.get('brand'))

# Adding data into dictionary
car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}

x = car.keys()
print(x) #before the change
car["color"] = "white"

print(x) #after the change