# Dragon Realm
import random
import time

def display():
    print('''You are in a land full of Dragons. In front of you,
        you see two caves. In one cave, the Dragon is friendly 
        and will share his treasure with you. The other Dragon
        is greedy and hungry , and will eat you on sight.''')
    print()
    
def chooseCave():
 Cavechoice = " "
 while Cavechoice != 1 and Cavechoice != 2 :
     print("Which Cave you wanna walk into player? (1 or 2): ")
     Cavechoice = int(input())
 return Cavechoice

def checkCave(chooseCave):
   print("You approach the Cave...")
   time.sleep(2)
   print("It is Dark and Spooky...")
   time.sleep(2)
   print("A large Dragon jumps out in front of you! He opens his jaws and ...")
   print()
   time.sleep(2)
   print("You still have an Escape! Will you switch the cave?(yes or no)")
   OptCave = input().lower()
   while OptCave != 'yes' and OptCave != 'no':
      print("You still have an Escape! Will you switch the cave?(yes or no)")
      OptCave = input().lower()

   if OptCave == 'yes':
      if chooseCave == 1:
         chooseCave = 2;
      else:
         chooseCave = 1;
   
   friendlyCave = random.randint(1,2)
   if chooseCave == friendlyCave :
      print("Gives you his treasure!")
   else:
      print("Gobbles you down with one bite!")


playAgain = "yes"
while playAgain == 'yes' or playAgain =='y':
   display()
   CaveNum = chooseCave()
   checkCave(CaveNum)

   print("Do you want to play Again?(yes or no)")
   playAgain = input().lower()



      



      
      





     


   
     