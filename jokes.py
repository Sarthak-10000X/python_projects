# Laugh out loud !!

while(True):
 Choice = int(input("\n Hey! There are 10 jokes! , Select from 1 to 10: "))
 match Choice:
    case 1:
        print("What do you get when you cross a Snowman with a Vampire !?")
        input()
        print("Frostbite!")
    case 2: 
        print("What do dentist call an Astronaut's cavity ?")
        input()
        print("A black hole!")
    case 3: 
        print("Knock Knock !")
        input()
        print("Interrupting cow")
        input()
        print("Interrupting cow w-", end="")
        print("MOOOOOOO")
    case 4: 
        print("How do you make a holy water ?")
        input()
        print("You boil the hell out of it!")
    case 5: 
        print("Parallel lines have so much in common....")
        input()
        print("It's a shame that they will never meet!")
    case 6:
        print("I asked my dog what two minus two..")
        input()
        print("He said nothing")
    case 7:
        print("If tomatoes are technically fruits..")
        input()
        print("Then ketchup is a smoothie")
    case 8:
        print("Why dont graveyards ever get overcrowded?")
        input()
        print("Because people are dying to get in !")
    case 9:
        print("Why is life like a Software Update ?")
        input()
        print("Whenever you finally get comfortable... it changes everything")
    case 10:
        print("Why don't echoes argue?")
        input()
        print("Because they always get the last word... twice.")
    case _:
        print("Heyy thanks!")
        break
    
