# String concatenation

# Method 1
p = "I"
l = "am"
m = "ok"
o = p + l + m
print(o)
k = p+" "+l+" "+m
print(k)

name1 = "Becky" 
age1 = 26
# result = name1+age1
# print(result)

result1 = name1+ str(age1)
print(result1)


# Method 2 
# print(p,l,m)


# Method 3 
n = " ".join([p,l,m])
print(n)

i = "".join([p,l,m])
print(i)

j = "-".join([p,l,m])
print(j)


# Method 4 
print("hello {}".format("benjamin"))

print("bye {}".format("rex"))

print("Hi my name is {} and i am{} years old".format("Bob",16))

print("Hi my name is{0} and i am {1} years old".format("Bob",16))

print("Hi my name is {1} and i am {0} years old".format("Bob",16))

print("Hi my name is {name} and i am {age} years old".format(name = "Bob",age = 16))



# Method 5 - fstring
name = "Samantha"
print(f"my name is {name}")

age = 83 
print(f"My age is {age}") 

print(f"My name is {name},My age is {age}")
