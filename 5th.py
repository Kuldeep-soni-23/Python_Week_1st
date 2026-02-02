# Q5. Write a program to find the largest of three numbers. 

a = int(input("Enter your a value: "))
b = int(input("Enter your b value: "))
c = int(input("Enter your c value: "))

if a>=b and a>=c:
    print("The largest number is a:", a)
elif b>=a and b>=c:
    print("The largest number is b:", b)
else:
    print("The largest number is c:", c)