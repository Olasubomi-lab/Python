marks = [1,4,10,15]
print(marks)

fruits = ["apple","orange","cranberry"]
print(fruits)

list1 = []
print(list1)

list2 = [1,"boss",True,None,1.32]
print(list2)




# List indexing - the lists are ordered

veg_list = ["lettuce","cauliflower","spinach"]
print(veg_list[0])
print(veg_list[2])
print(veg_list[-2])
      

 
# Replacing list elements - lists are mutabl

colours = ["blue","white","green"]
print(colours)
colours[2] = "yellow"
print(colours)


numbers = [6,12,18,24,30,36,42,48]
numbers[0:4] = [3,7,1,5]
print(numbers)





# List joining


flowers = ["daisys","spiderlily","rose"]
print(flowers)
flowers.append("tulip")
print(flowers)
flowers.extend(["sunflower","iris"])
print(flowers)





# Element deletion
# 1 del statement

animals = ["lion","mouse","tulip","rhino"]
del animals[2]
print(animals)

# list3 = [1,4,6,3]
# del list3
# print(list3)          : leaves an error



# 2 . remove function 
pet = ["lion","hamster","cat","snake",]
print(pet)
pet.remove("lion")
print(pet)


# Sorting a list
num = [76,34,5,1]
num.sort()                          #ascending order   
print(num)

num1 = [76,34,5,1]
num1.sort(reverse=True)            #descending order
print(num1)


things = ["book","a","king"]
things.sort()
print(things)


# .join method

names = ["david","kayla","simon"]
print(names)
new_names = "-".join(names)
print(new_names)
new_names1 = "*".join(names)
print(new_names1)

# items = ["string","paper",30]     
# items_2 = "-".join(items)
# print(items_2)                   # leaves an error 




# list copy
original = [6,2,63,25]
print(original)
clone = original
print(clone)

original[0] = 75
print(original)
print(clone)

original1 = [103,42,61,59]
clone1 = original1.copy()
original1[0] =  500
print(original1)
print(clone1)


# Built in list functions
numbers = [53,91,43,91,12]
print(numbers.count(91))

print(numbers.index(53))
print(numbers.index(91))

numbers.reverse()
print(numbers)

print(max(numbers))
print(min(numbers))
print(sum(numbers))