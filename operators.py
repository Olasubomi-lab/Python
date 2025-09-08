# Types of operators in python

# Arithmetic operators
a = 10
b = 4
print(a+b)      #addition
print(a-b)      #subtraction
print(b*a)      #multiplication
print(a/b)      #division
print(a//b)     #floor divison
print(a%b)      #Modulus 
print(a**b)     #exponent


# Assignment operators
c = 62
c+=7
print(c)

# Relational operators

r = 13
y = 11
print(r == y)
print(r != y)
print(r > y)
print(r < y)
print(r >= y)
print(r <= y)


# Logical operators

h = 89
t = 3
# 1. and
print(h > 3 and t < 10)
print(h < 3 and t < 10)
print(h < 3 and t > 10)

# 2. or
print(h > 3 or t < 10)
print(h < 3 or t < 10)
print(h < 10 or t > 10)

# 3. not
print(t < 10)
print(not(t<10))