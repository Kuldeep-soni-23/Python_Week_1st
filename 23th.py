# Q23. Write a Python program to print a pattern of stars in a triangle. 
n = int(input("Enter number of rows: "))

for i in range(1, n + 1):
    for j in range(i):
        print("*",end = "")
    print()
