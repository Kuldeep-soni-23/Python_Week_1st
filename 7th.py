# Q7. Write a program to calculate the factorial of a number using a loop. 

num = int(input("Enter a number: "))
factorial = 1
if num < 0:
    print("Factorial is not defined for negative numbers.")
elif num == 0 or num == 1:
    print("The factorial of", num, "is 1")
else:
    for i in range(2, num + 1):
        factorial *= i
    print("The factorial of", num, "is ", factorial)
