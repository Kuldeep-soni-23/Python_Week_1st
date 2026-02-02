# Q10. Check if a number is a palindrome. 

num = int(input("Enter the number"))
orignal = num
reversed = 0

while num>0:
    remainder = num%10
    reversed = reversed * 10 + remainder
    num//=10

if orignal == reversed:
    print(orignal , "is palindrome")
else:
    print(orignal,"not Palindrome")