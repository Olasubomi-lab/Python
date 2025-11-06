#Example 1: printing numbers from 1-5

i = 1
while i <= 5:
    print(i)
    i+=1

print()

#Example 2: print even numbers from 2-10

i = 2
while i <= 10:
    print(i)
    i+=2

print()


# Example 3: print odd numbers from 1-10

i = 1
while i <= 10:
    print(i)
    i+=2

print()


#Example 4: Countdown

count = 5
while count >0:
    print(count)
    count-=1


# Example 5: Sum of first 5 natural numbers

i = 1
total = 0 
while i <= 5:
    total+= i
    i+=1
print("Sum",total)


# # Example 6: Take input until user types exit
# text = ""
# while text != "exit":
#     text = input("type exit to stop")

print()
# Example 7: Take input umtil user types 0 
num = None
while num != 0:
    num = int(input("Enter the number 0 to stop"))

# Example 8: Infinite loop
while True:
    print("This will run forever")