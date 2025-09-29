tuple1 = (1,4,65,3,2,6,98)
print(tuple1)


tuple2 = ()
print(tuple2)

tuple3 = 2,54,1,9,57,43,73
print(tuple3)


list_ex = ["book","boat","blast"]
print(list_ex)

tuple_ex = tuple(list_ex)
print(tuple_ex)


# tuple elements have an index - tuples are ordered

tuple4 = (1.3,3.6,2.6,"chicken",53,21,"porcupine")
print(tuple4[1])
print(tuple4[0:3])
print(tuple4[:4])
print(tuple4[2:])
print(tuple4[::2])
print(tuple4[::1])
print(tuple4[::-1])
print(tuple4[::-2])



# Tuples are immutuable - elements of a tuple cannot be changed

# tuple5 = (2,4,6,8,10,83)
# tuple5[5] = 12
# print(tuple5)


# Joining tuples

tuple6 = ( 1,3,5,7,9)
tuple7 = (7,14,21,28,35)
tuple8 = tuple6+tuple7 
print(tuple8)



# deleting tuples
# tuple9 = (0,90,98,78,67)
# print(tuple9)
# del tuple9
# print(tuple9)



# Tuple functions

tuple56 = (92,11,74,654,92)
print(tuple56.count(92))
print(tuple56.index(11))
print(tuple56.index(92))

print(len(tuple56))
print(max(tuple56))
print(min(tuple56))


sorted_tuple = sorted(tuple56)
print(sorted_tuple)
real_tuple = tuple(sorted_tuple)
print(real_tuple)


sorted_tuple = tuple(sorted(tuple56))
print(sorted_tuple)