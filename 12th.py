# Q12. Create a number guessing game. 
import random
num = int(input("Enter your number: "))
guessing_num = random.randint(1, 100)
print("guessing number: ",guessing_num)
if guessing_num == num:
    print("Game is Wining")
else:
    print("Game not wining")]