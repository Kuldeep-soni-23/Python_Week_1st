#Q11. Write a program to find the sum of first N natural numbers. 
num = int(input("Enter a positive integer: "))
if num < 1:
    print("Please enter a positive integer.")
else:
    sum = 0
    for i in range(1, num+1):
        sum += i
    print("The sum of the first", num, "natural numbers is:", sum)