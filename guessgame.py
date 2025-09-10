import random
target= random.randint(1,100)
attempts=0
max_attempts=6
print("guess the number from 1 to 100")
while (attempts < max_attempts):
 try:  
  guess= int(input(f" Attempt {attempts+1}: "))
  attempts+=1

  if guess == target:
        print(f"CONGRATULATION, {guess} is correct!")
        break
  elif (guess < target):
        print("guessed number is low, attempt higher!")
  else:
        print("guessed number is high, attempt lower!")

  if (guess != target and attempts == max_attempts):
        print(f"Hard luck!, the number was {target}")
        break
 except ValueError:
  print("INVALID NUMBER PLEASE ENTER A VALID NUMBER")
 






    
