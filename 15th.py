# Q15. Create a program to print the Fibonacci series up to N terms. 
num = int(input("Enter your number: "))
a = 0
b = 1
if num <= 0:
    print("put the positive number")
elif num == 1:
    print(f"{a} is fibonaci")
else:
    print("fibonaci series")
    print(a,end = "")
    for i in range(2,num):
        c = a+b
        print(c," ")
        a = b
        b = c
 
