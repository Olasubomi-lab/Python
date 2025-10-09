set1 = {1,5,278,43,26}
print(set1)

set2 = set([2.5,764,76324,64])
print(set2)

# Sets do not allow duplicate items
set3 = {23,73,23,534,"hello","hello"}
print(set3)

# Sets are mutable you can edit them
set4 = {"four",4.3,9,3,4,"y"}
print(set4)
set4.add("rice")
print(set4)

# Set operation number 1 - Union
set5 = {"blast","grass","5"}
set6 = {"quiet","air",10}
print(set5|set6)
print(set5.union(set6))

# Set operation number2 - Intersection
set7 = {"0",1,2}
set8 = {"zero",2,"keyboard"}
print(set7 & set8)
print(set7.intersection(set8))

# Set operations number3 - Difference
set9 = {1,2,3,4,5}
set10 = {3,4,5,6,7}
print(set9-set10)
print(set9.difference(set10))

# Set operations number4 - Symmetric difference
set11 = {1,2,3}
set12 = {3,4,5}
print(set11^set12)
print(set11.symmetric_difference(set12))

