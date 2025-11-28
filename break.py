# Example 1 - stop a loop when a number is found

for i in range(1,11):
    if i == 5:
        break
    print(i)

# Example 2 - stop a loop when an element in a list is found
foods = ["burger","pizza","rice","bread"]
for i in foods:
    if i == foods[2]:
        break
    print(i)

print()
# Example 3

fruits = ["burges","pizza","rice","bread"]
for i in fruits:
    if i == fruits[2]:
        print(i)
        break
    
print()

# Example 4 - find the first even number

even = [1,93,5,17,6,5,39]

for i in even:
    if i%2==0:
        print(i)
        break

