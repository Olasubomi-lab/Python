num1 = int(input("Enter first number"))
num2 = int(input("Enter second number"))

try:
    num3 = num1/num2
except:
    print("Dividing these numbers is not possible")
else:
    print(f"These numbers are divisible. Result:{num3}")
finally:
    print("This code is about handling 0 division error")