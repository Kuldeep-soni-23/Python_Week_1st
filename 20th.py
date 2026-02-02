# Q20. Create a program to find the second largest number in a list. 
num = [10, 20, 4, 45, 99]
for i in range(len(num)):
    for j in range(i + 1, len(num)):
        if num[i] > num[j]:
            temp = num[i]
            num[i] = num[j]
            num[j] = temp
print("The second largest number is:", num[-2])