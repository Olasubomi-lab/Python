# Example 1
def num():
    global age
    age = 5
    print (age)
num()
print(age)



# Example 2
def greet():
    global message
    message = "hello"
    print(message)
greet()
print(message)




# Example 3
def square(num):
    global squared
    squared = num*num
    print(squared)
square(4)
print(squared)