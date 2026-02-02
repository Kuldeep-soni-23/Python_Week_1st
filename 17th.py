# Q17. Write a program to find the LCM of two numbers. 
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
max_num = max(a, b)
lcm = max_num
while True:
    if lcm % a == 0 and lcm % b == 0:
        break
    lcm += max_num
print("LCM is:", lcm)