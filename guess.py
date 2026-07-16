#Guess the number!
import random as random
print("Hello! Whats your name?")
name = input()
print(f"Well , {name} I am thinking of a number from 1 to 50!")
number = random.randint(1,50)
guessTaken0=0
for guessTaken in range(5):
    guess = int(input(f"Guess the number: "))
    if(guess == number):
        break
    elif(guess > number):
        print("The number is too large!")
    elif(guess < number):
        print("The number is too small!")

if guess == number :
    print(f"Congratulation! You guessed my number in {guessTaken+1} moves")
elif guess != number :
    print(f"No worries, The number is {number}")
 
