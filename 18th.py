# Q18. Check whether a character is a vowel or consonant. 
char = input("Enter the Character: ")
vowels = {'a','e','i','o','u','A','E','I','O','U'}
if char in vowels:
    print("Character is a vowel")
else:
    print("Character is a consonant")
