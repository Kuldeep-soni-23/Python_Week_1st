# Q28. Write a program to find the sum of all even numbers in a list. 
num = int(input("Enter the number of elements in the list: "))
numbers = []
sum_even = 0
for i in range(1, num + 1):
    if i % 2 == 0:
        sum_even += i
print("Sum of all even numbers from 1 to", num, "is:", sum_even)