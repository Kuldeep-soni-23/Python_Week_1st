# Q8. Create a program to count the number of vowels in a string. 

str = input("Enter the string: ")
vowels = {'a','e','i','o','u','A','E','I','O','U'}

count = 0
for i in str:
    if i in vowels:
        count += 1
print("Number of vowels in the given string is:", count)
