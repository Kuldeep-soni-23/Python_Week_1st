# Q25. Write a program to display the ASCII value of a character. 

ch = input("Enter a character: ")

for i in range(256):
    if chr(i) == ch:
        print("ASCII value of", ch, "is", i)
        break
# ch = input("Enter a character: ")

# print("ASCII value of", ch, "is", ord(ch))
