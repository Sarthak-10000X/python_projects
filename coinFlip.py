#Coin flip simulation
import random

print("Simulating coin flips 1000 times guess how many times it comes heads!(press enter to begin)")
input()
heads = 0
flips = 0

while flips < 1000 :
    if random.randint(0,1) == 1:
        heads += 1
    flips += 1

    if flips == 100:
        print('At 100 tosses the head comes ' + str(heads) + ' times')
    if flips == 500:
        print('Halfway there ! , the head comes ' + str(heads) + ' times')
    if flips == 900:
        print('At 900 tosses the head comes ' + str(heads) + ' times')

print()
print('Out of 1000 coin flips head comes ' + str(heads) + ' times!')
