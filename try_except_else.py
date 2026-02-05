num1 = int(input("Enter first number"))
num2 = int(input("Enter second number"))

try: 
    num3 = num1/num2
except:
    print("Impossible to divide")
else:
    print(f"Division succesful. Result:{num3}")


