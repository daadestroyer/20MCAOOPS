# Loop Through a Dictionary and get only keys
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
for x in thisdict:
    print(x) 
    

# Loop Through a Dictionary and get only values
print()
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
for x in thisdict:
    print(thisdict[x]) 

# Getting keys using {You can also use the keys() method to return values of a dictionary:}
print()
for x in thisdict.keys():
    print(x)    


# Getting values using {You can also use the values() method to return values of a dictionary:}
print()
for x in thisdict.values():
    print(x)


# Getting keys and values using {You can also use the items() method to get keys and values:}
print()
for x,y in thisdict.items():
    print(x,y)

