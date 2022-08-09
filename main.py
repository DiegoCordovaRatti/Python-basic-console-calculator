from math import sqrt, pow
print("Enter 2 numbers and get different results")

num1 = input("Enter your number: ")
num2 = input("Enter your second number: ")
result1 = float(num1) + float(num2)
result2 = float(num1) - float(num2)
result3 = float(num1) * float(num2)
result4 = float(num1) / float(num2)
result5 = pow(float(num1), float(num2))
result6 = pow(float(num2), float(num1))


print("- " + max(num1, num2) + " is greater than " + min(num1, num2))
print("- " + min(num1, num2) + " is less than " + max(num1, num2))
print("- The result of " + str(num1) + " + " + str(num2) + " is = " + str(result1))
print("- The result of " + str(num1) + " - " + str(num2) + " is = " + str(result2))
print("- The result of " + str(num1) + " * " + str(num2) + " is = " + str(result3))
print("- The result of " + str(num1) + " / " + str(num2) + " is = " + str(result4))
print("- The result of " + str(num1) + " raised to the power " + str(num2) + " is = " + str(result5))
print("- The result of " + str(num2) + " raised to the power " + str(num1) + " is = " + str(result6))
print("- The square root of " + str(num1) + " is = " + str(sqrt(float(num1))))
print("- The square root of " + str(num2) + " is = " + str(sqrt(float(num2))))



