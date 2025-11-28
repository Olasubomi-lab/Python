# Example 1 - skip printing the number 5

for i in range(1,11):
    if i == 5:
        continue
    print(i)


# Example 2 - skip odd numbers

for i in range(1,11):
    if i%2 != 0:
        continue
    print(i)

# Example 3 - skip empty strings in a list

characters = ["Harry","dan","","mice",""]

for i in characters:
    if i == "":
        continue
    print(i)

# Example 4 - skip a particular element in a list

thing = ["air","water","fire","earth"]

for i in thing:
    if i == thing[2]:
        continue
    print(i)