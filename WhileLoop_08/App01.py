'''
Python Loops
Python has two primitive loop commands:

while loops
for loops
'''

i = 0
while i <= 10:
    print(i)
    i += 1

# The break Statement
print()

i = 1
while i < 6:
    print(i)
    if i == 3:
        break
    i += 1

# The continue Statement
print()
i = 0
while i < 6:
    i += 1
    if i == 3:
        continue
    print(i)
