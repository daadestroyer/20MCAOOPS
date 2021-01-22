a = "hello world !"
print(a[0]+":"+a[1]+":"+a[2]+":"+a[3]+":"+a[4]+":"+a[5]+":"+a[6]+":"+a[7]+":"+a[8]+":"+a[9]+":"+a[10])

# Looping Through a String
print()
for x in "banana":
  print(x)

# String Length
print()

print(len(a))

# Check String
# To check if a certain phrase or character is present in a string, we can use the keyword in.
print()

# check if present in txt
txt = "The best things in life are free!"
print("free" in txt) # true

# check using if
text = "The best things in life are free!"
if "free" in text :
    print("present") # present

# check if not present in text
text1 = "The best things in life are free!"
print("expensive" not in text1)

# check using if
if "expensive" not in text1:
    print("yes")