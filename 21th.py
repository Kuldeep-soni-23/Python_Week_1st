# Q21. Write a program to count the number of digits in an integer. 

num = int(input("Enter your number: "))
count = 0
for i in str(num):
    count += 1
print("Number of digits is:", count)