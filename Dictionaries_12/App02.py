# Change Values
thisdict = {
    "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

thisdict["year"] = 2018
print(thisdict.get('year'))

# Update Dictionary
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.update({"year": 2020})
print(thisdict)

# Adding Items
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict["color"] = "red"
print(thisdict)

# Removing Items {The pop() method removes the item with the specified key name:}
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.pop("model")
print(thisdict)

# Removing Items {The popitem() method removes the last inserted item (in versions before 3.7, a random item is removed instead):}
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.popitem()
print(thisdict)

# Delete dictionary {The del keyword removes the item with the specified key name: and dictionary object also not exist}
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
del thisdict["model"]
print(thisdict)

# Clear dictionary {The clear() method empties the dictionary: and dictionary object exit}
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.clear()
print(thisdict)