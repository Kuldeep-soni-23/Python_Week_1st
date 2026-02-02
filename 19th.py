# Q19. Write a program to calculate the sum of digits of a number. 
num = int(input("Enter your number: "))
sum = 0
for i in str(num):
    count = int(i)
    sum += int(i)
print("Sum of digits is:", sum)